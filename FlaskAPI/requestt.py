import requests

from Data_input import data_in

URL = "http://127.0.0.1:5000/predict"

response = requests.post(
    URL,
    json={"input": data_in},
    timeout=30,
)
response.raise_for_status()
print(response.json())
