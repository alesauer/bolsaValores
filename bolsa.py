import yfinance as yf
import matplotlib.pyplot as plt

#Lista de símbolos das ações
acoes = ['ITSA4.SA', 'PETR4.SA', 'VALE3.SA', 'BBDC4.SA', 'ABEV3.SA']

#Obter os dados históricos para cada ação

dados_acoes = {}

for acao in acoes:
    dados_acoes[acao] = yf.download(acao, start='2024-01-01', end='2024-12-31')

#Gerar os graficos
plt.figure(figsize=(12,8))

for acao, dados in dados_acoes.items():
    plt.plot(dados.index, dados['Close'], label=acao)

plt.title("Histórico de Precos de Açoes")
plt.xlabel("Data")
plt.ylabel("Preco de Fechamentos")
plt.legend()
plt.grid(True)
plt.show()
