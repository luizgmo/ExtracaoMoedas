import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
# print (cotacoes)
print("Dolar hoje: R${:.4}".format(cotacao_dolar))
print("Euro hoje: R${:.4}".format(cotacao_euro))
print("Bitcoin hoje: R${}".format(cotacao_bitcoin))