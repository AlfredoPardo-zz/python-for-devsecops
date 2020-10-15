import requests; import os; from datetime import datetime

headers = {
    'Authorization': 'ApiKey admin:your-api-key-goes-here'
}

folder = "./inputs"; file = "retire.json";
current_date = datetime.now().strftime("%Y-%m-%d")
engagement_id = 1
api_protocol="http"; api_url = "127.0.0.1"; api_port=8080

files = {
    'file': (file, open(os.path.join(folder,file), 'rb')),
    'scan_type': (None, 'Retire.js Scan'),
    'tags': (None, 'py-requests'),
    'verified': (None, 'true'),
    'active': (None, 'true'),
    'scan_date': (None, current_date),
    'engagement': (None, '/api/v1/engagements/{}/'.format(engagement_id)),
}

response = requests.post('{}://{}:{}/api/v1/importscan/'.format(api_protocol, api_url, api_port), 
headers=headers, files=files)