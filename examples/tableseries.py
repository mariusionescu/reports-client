
from random import randint
from reports_client.client import ReportClient
from datetime import datetime, timedelta

reports_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)


def add_data():

    for i in range(300):
        rows = []
        for j in range(500):
            rows.append({"username": "user_%s" % j, "visits": randint(1, 10), "impressions": randint(10, 100)})
        date = datetime.utcnow() - timedelta(days=1000 - i)
        reports_client.push(rows, index="username", timestamp=date)


def delete_data():
    reports_client.delete()


def get_data():
    start_date = datetime.utcnow() - timedelta(days=1000)
    end_date = datetime.utcnow() - timedelta(days=490)
    data = reports_client.read(start_date=start_date, end_date=end_date, aggregation={'visits': 'mean'})
    print data

