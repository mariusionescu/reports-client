# reports-client

## Installation

    cd /tmp
    git clone https://github.com/mariusionescu/reports-client.git
    cd reports-client
    python setup.py install
    
# Usage
 
## Time series

    from reports_client.client import ReportClient
    reports_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
     
    rows = {"user_count": 10}
        
    reports_client.push(rows)

## Time tables
    
    from reports_client.client import ReportClient
    reports_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
     
    rows = [{"process": "top", "cpu": 10, "memory": 3023}, {"process": "apache2", "cpu": 87, "memory": 20123}]
        
    reports_client.push(rows, index="process")
    
## Get data
    from reports_client.client import ReportClient
    reports_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
    
    reports_client.read()
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=2)
    
    reports_client.read(start_date=start_date, end_date=end_date)
    