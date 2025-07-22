import pandas as pd
import os
import matplotlib.pyplot as plt


caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\30 - Análise de dados com Python e Pandas\datasets'

arq1 = "Aracaju.xlsx"
arq2 = "Fortaleza.xlsx"
arq3 = "Natal.xlsx"
arq4 = "Recife.xlsx"
arq5 = "Salvador.xlsx"

df1 = pd.read_excel(os.path.join(caminho, arq1))
df2 = pd.read_excel(os.path.join(caminho, arq2))
df3 = pd.read_excel(os.path.join(caminho, arq3))
df4 = pd.read_excel(os.path.join(caminho, arq4))
df5 = pd.read_excel(os.path.join(caminho, arq5))

df = pd.concat([df1, df2, df3, df4, df5])

# criando coluna receita
df['Receita'] = df['Vendas'].mul(df['Qtde'])

# transformando a coluna de data em tipo data
df["Data"] = pd.to_datetime(df["Data"])

# criar coluna de anos
df['Ano_Venda'] = df['Data'].dt.year

# criando coluna - extraindo mes e dia
df['Mes_venda'], df['Dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

# criando coluna com calculando a diferença de dias
df['Diferença_de_dias'] = df['Data'] - df['Data'].min()

# criando coluna de trimestre
df['Trimestre_venda'] = df['Data'].dt.quarter

# filtra as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Mes_venda'] == 3)]

print(vendas_marco_19)

print(df.sample(10))

# contagem de vendas através do número de linhas com o mesmo LojaID
print(df['LojaID'].value_counts(ascending=False))

# localizando vendas com um determinado número de ID
print(df.loc[df['LojaID'] == 1003])

# grafico de barras vertical
df['LojaID'].value_counts(ascending=False).plot.bar()
plt.show()

# grafico barras horizontais
df['LojaID'].value_counts(ascending=True).plot.barh()
# apresentando o grafico
plt.show()

# grafico pizza
df.groupby(df['Ano_Venda'])['Receita'].sum().plot.pie()
plt.show()

print(df['Cidade'].value_counts())

# adicionando um titulo e alterando o nome dos eixos
df['Cidade'].value_counts().plot.bar(title='Total Vendas por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Total Vendas')
plt.show()

# https://web.dio.me/lab/analise-de-dados-com-python-e-pandas/learning/ce5be393-b336-4384-8983-f3550e23e8ac
# parei no minuto 6:50h
