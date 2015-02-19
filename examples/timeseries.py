
from random import randint
from reports_client.client import ReportClient
from datetime import datetime, timedelta
reports_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)


def add_data():

    for i in range(1000):
        rows = {"user_count": randint(100, 200)}
        date = datetime.utcnow() - timedelta(days=1000 - i)
        reports_client.push(rows, timestamp=date)


def delete_data():
    reports_client.delete()


def get_data():
    start_date = datetime.utcnow() - timedelta(days=1000-900)
    end_date = datetime.utcnow() - timedelta(days=10)
    data = reports_client.read(start_date=start_date, end_date=end_date)
    print data
