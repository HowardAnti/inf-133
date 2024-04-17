import requests

url = "http://localhost:5000/"

response = requests.get(url)
print(response.text)

urls = url+"/saludar?nombre=Howard"

response = requests.get(urls)
print(response.text)


urlsum = url+"/sumar?num1=5&num2=3"
response = requests.get(urlsum)
print(response.text)

urlpal = url+"/palindromo?cadena=hannah"
response = requests.get(urlpal)
print(response.text)

urlcont = url+"/contar?cadena=exepcioneeeeeeeeeeeees&vocal=e"
response = requests.get(urlcont)
print(response.text)