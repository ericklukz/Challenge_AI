import requests

data = {'texto': 'Computador que rode GTA V'}

url = 'http://localhost:5000/receber-texto'

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)