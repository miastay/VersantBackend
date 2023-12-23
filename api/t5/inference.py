import json
import requests

## secrets.json format:
#
#   {
#       key: <API_KEY>
#   }
#
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../t5/secrets.json")
with open(path, "r") as read_file:
    data = json.load(read_file)

API_URL = "https://api-inference.huggingface.co/models/Falconsai/medical_summarization"
headers = {"Authorization": f"Bearer {data['key']}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()
    print(output)
    return output