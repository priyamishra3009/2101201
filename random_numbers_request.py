import requests

response = requests.get("http://20.244.56.144/test/rand")
print(response.json())