from urlparse import urlparse
from httplib import HTTPConnection
import config
import json
import time


class ReportClient(object):
    def __init__(self, key, report_id):
        self.key = key
        self.report_id = report_id
        self.url = '%s/%s/' % (config.REPORTS_API, report_id)
        url_parts = urlparse(self.url)

        self.path = url_parts.path
        self.connection = HTTPConnection(url_parts.netloc, url_parts.port or 80)
        self.data = {'key': key}

    def push(self, rows, index=None):
        data = self.data.copy()
        data['rows'] = rows
        data['timestamp'] = time.time()

        if index:
            data['index'] = index

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
            return False

    def read(self, aggregation=None):
        data = self.data.copy()
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
            return False

    def delete(self):
        data = self.data.copy()
        self.connection.request('DELETE', self.path, data)
        response = self.connection.getresponse()

        try:
            response_data = json.loads(response.read())
        except ValueError:
            response_data = {}

        if response_data.get('success'):
            return True
        else:
            return False