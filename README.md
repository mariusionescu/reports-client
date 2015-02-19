# reports-client

## Installation

    cd /tmp
    git clone https://github.com/mariusionescu/reports-client.git
    cd reports-client
    python setup.py install
    
## Usage

    from report_client.client import ReportClient
    report_client = ReportClient(key='AMJ1IG2N4UEJUR2K', report_id=1)
     
    rows = {"user_count": "10"}    
