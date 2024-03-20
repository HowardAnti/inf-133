import requests
url = "http://localhost:8000"

url_a = url + "/posts"
response = requests.get(url_a)

print(response.text)

url_b = url + "/post/2"
response = requests.get(url_b)

print(response.text)

url_c = url + "/posts"

my_expericience = {
    "title": "Mi experiencia como dev",
    "content": "Ninguna :v",
}

response = requests.post(url_c, json=my_expericience,  headers={'Content-type': 'application/json'})



print(response.text)

url_d = url + "/post/3"

my_expericience_updated = {
    "title": "Mi experiencia como dev",
    "content": "En progreso",
}

response = requests.put(url_d, json=my_expericience_updated,  headers={'Content-type': 'application/json'})

print(response.text)

url_e = url + "/post/2"

response = requests.delete(url_e)
print(response.text)


url_a = url + "/posts"
response = requests.get(url_a)

print(response.text)