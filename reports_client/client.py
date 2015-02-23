from urlparse import urlparse
from httplib import HTTPConnection
import config
import json
import time
from datetime import datetime


class InvalidKey(Exception):
    pass


class InvalidPayload(Exception):
    pass


class InvalidSchema(Exception):
    pass


class EmptyDB(Exception):
    pass


class GenericReportException(Exception):
    pass

EXCEPTION_MAP = {
    'INVALID_KEY': InvalidKey,
    'INVALID_PAYLOAD': InvalidPayload,
    'INVALID_SCHEMA': InvalidSchema,
    'EMPTY_DB': EmptyDB
}


class ReportClient(object):
    def __init__(self, key, report_id):
        self.key = key
        self.report_id = report_id
        self.url = '%s%s/' % (config.REPORTS_API, report_id)
        url_parts = urlparse(self.url)

        self.path = url_parts.path
        self.connection = HTTPConnection(url_parts.netloc, url_parts.port or 80)
        self.data = {'key': key}

    def push(self, rows, index=None, timestamp=None):
        data = self.data.copy()
        data['rows'] = rows
        data['timestamp'] = time.time()

        if index:
            data['index'] = index

        if timestamp:
            timestamp = (timestamp - datetime(1970, 1, 1)).total_seconds()
            data['timestamp'] = timestamp

        raw_data = json.dumps(data)
        self.connection.request('PUT', self.path, raw_data)
        response = self.connection.getresponse()

        try:
            response_data = json.loads(response.read())
        except ValueError:
            response_data = {}

        if response_data.get('success'):
            return True
        else:
            error = response_data.get('error')
            message = response_data.get('message', "That's all")
            exception = EXCEPTION_MAP.get(error, GenericReportException)
            raise exception(message)

    def read(self, aggregation=None, start_date=None, end_date=None):
        data = self.data.copy()

        if start_date:
            start_date = (start_date - datetime(1970, 1, 1)).total_seconds()
            data['start_date'] = start_date

        if end_date:
            end_date = (end_date - datetime(1970, 1, 1)).total_seconds()
            data['end_date'] = end_date

        if aggregation:
            data['aggregation'] = aggregation

        raw_data = json.dumps(data)
        self.connection.request('POST', self.path, raw_data)
        response = self.connection.getresponse()

        try:
            response_data = json.loads(response.read())
        except ValueError:
            response_data = {}

        if response_data.get('success'):
            return response_data.get('data')
        else:
            error = response_data.get('error')
            message = response_data.get('message', "That's all")
            exception = EXCEPTION_MAP.get(error, GenericReportException)
            raise exception(message)

    def delete(self):
        data = self.data.copy()
        raw_data = json.dumps(data)
        self.connection.request('DELETE', self.path, raw_data)
        response = self.connection.getresponse()

        try:
            response_data = json.loads(response.read())
        except ValueError:
            response_data = {}

        if response_data.get('success'):
            return True
        else:
            error = response_data.get('error')
            exception = EXCEPTION_MAP.get(error, GenericReportException)
            raise exception