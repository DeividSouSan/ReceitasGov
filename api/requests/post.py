import json
import os
import requests

def send_post_request(url: str, log: bool = False):
    with open(f"{os.getcwd()}/output/output.json", 'r', encoding='utf-8') as f:
        data_json = json.loads(f.read())
        
    response = requests.post(url, json=data_json)
    
    with open(f"{os.getcwd()}/response.txt", 'w', encoding='utf-8') as f:
        f.write(f"Status da requisição: {response.status_code}")