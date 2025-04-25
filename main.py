import requests 
import pandas as pd
from datetime import datetime

# 1. Coleta de dados da API
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
response = requests.get(url)
data = response.json()

# 2. Transformar os dados em uma estrutura legível
moedas = ['USDBRL', 'EURBRL', 'BTCBRL']
linhas = []

for moeda in moedas:
    info = data[moeda]
    linhas.append({
        'moeda': moeda,
        'nome': info['name'],
        'cotacao': float(info['bid']),
        'data': datetime.fromtimestamp(int(info['timestamp']))
    })

df = pd.DataFrame(linhas)

# 3. Salvando como CSV
df.to_csv("cotacoes.csv", index=False)
print("CSV gerado com sucesso!")

# 4. Análise simples
print("\nResumo das cotações:")
print(df.describe())

print("\nMaior cotação:")
print(df[df['cotacao'] == df['cotacao'].max()])