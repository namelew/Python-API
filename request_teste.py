import requests

base = "http://127.0.0.1:5000/"

#response = requests.put(base + "video/4", {"name":"Teste","likes":10, "views":2000})
#print(response.json())

response = requests.get(base + "video/1")
print(response.json())