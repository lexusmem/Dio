import pandas as pd
import os

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

print(df1.head())

df = pd.concat([df1, df2, df3, df4, df5])

# criando coluna receita
df['Receita'] = df['Vendas'].mul(df['Qtde'])

print(df.describe())

print(df.dtypes)

print(df.sample(5))

# verificar se consta nulo
print(df.isnull().sum())

# transformando a coluna de data em tipo inteiro
df['Data'] = df["Data"].astype('int64')

print(df.dtypes)

# transformando a coluna de data em tipo data
df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)

# agrupamento por ano
print(df.groupby(df["Data"].dt.year)['Receita'].sum())

# criar coluna de anos
df['Ano_Venda'] = df['Data'].dt.year

print(df['Ano_Venda'].max())
print(df['Ano_Venda'].min())

# extraindo mes e dia
df['Mes_venda'], df['Dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

print(df.sample(10))

# calculando a diferença de dias
df['Diferença_de_dias'] = df['Data'] - df['Data'].min()

print(df.sample(10))

# criando coluna de trimestre
df['Trimestre_venda'] = df['Data'].dt.quarter

print(df.sample(10))

# filtra as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Mes_venda'] == 3)]

print(vendas_marco_19)
