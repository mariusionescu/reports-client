# reports-client

## Installation

    cd /tmp
    git clone https://github.com/mariusionescu/reports-client.git
    cd reports-client
    python setup.py install
    
# Usage
 
## Time series

    from report_client.client import ReportClient
    report_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
     
    rows = {"user_count": 10}
        
    report_client.push(rows)

## Time tables
    
    from report_client.client import ReportClient
    report_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
     
    rows = [{"process": "top", "cpu": 10, "memory": 3023}, {"process": "apache2", "cpu": 87, "memory": 20123}]
        
    report_client.push(rows, index="process")
    
## Get data
    from report_client.client import ReportClient
    report_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
    
    report_client.read()
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=2)
    
    report_client.read(start_date=start_date, end_date=end_date)
    