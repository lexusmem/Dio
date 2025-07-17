import json
from urllib.request import urlopen
from pprint import pprint

url = 'http://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

for dado in dados:
    print(f'{dado} = {dados[dado]}')

pprint(dados)
