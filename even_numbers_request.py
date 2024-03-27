import requests

response = requests.get("http://20.244.56.144/test/even")
print(response.json())