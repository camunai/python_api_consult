import requests #  uso de requisições http 
import re #  uso de expressões regulares


url = 'https://jsonplaceholder.typicode.com/comments' # url da api

response = requests.get(url)

response_json = response.json()

# Imprime apenas os emails .org

for lista_de_email in response_json: 
    consulta = (re.findall(r'[\w\.-]+@[\w\.-]+\.org', lista_de_email['email']))
    if len(consulta) != 0:
        print(consulta) 
