from zeep import Client

client = Client("http://localhost:8000")


result = client.service.Saludar("Howard")
print(result)

result2 = client.service.SumaDosNumeros(4,5)
print(result2)

result3 = client.service.CadenaPalindromo("hannah")
print(result3)