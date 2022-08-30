import requests

url = 'http://127.0.0.1:8000/orders'

json = {
  "txid": "jhfdjhfdjh3djhfd4322ffmYw73v",
  "calendario": {
    "expiracao": 3600 
    },
  "devedor": {
    "cpf": "07490113512",
    "nome": "LUCAS DA SILVA DOS SANTOS"
    },
  "valor": {
    "original": "1.50"
    },
  "chave": "65906cbf-abea-4fe1-ad2a-c0e1e719f36b",
  "solicitacaoPagador": "Cobrança dos serviços prestados."
}

post = requests.post(url, json=json)
print(post)