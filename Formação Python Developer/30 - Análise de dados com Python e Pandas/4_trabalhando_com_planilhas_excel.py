import pandas as pd
import os

caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\30 - Análise de dados com Python e Pandas\datasets'

arq1 = 'Aracaju.xlsx'
arq2 = 'Fortaleza.xlsx'
arq3 = 'Natal.xlsx'
arq4 = 'Recife.xlsx'
arq5 = 'Salvador.xlsx'

df1 = pd.read_excel(os.path.join(caminho, arq1))
df2 = pd.read_excel(os.path.join(caminho, arq2))
df3 = pd.read_excel(os.path.join(caminho, arq3))
df4 = pd.read_excel(os.path.join(caminho, arq4))
df5 = pd.read_excel(os.path.join(caminho, arq5))

# imprimir as primeiras 5 linhas
print(df3.head())

# concatenar os df's
df = pd.concat([df1, df2, df3, df4, df5])

# imprimir as primeiras 5 linhas
print(df.head())

# imprimir as últimas 5 linhas
print(df.tail())

# imprimir uma amostra dos dados
print(df.sample(5))

# verificar os tipos de dados das colunas
print(df.dtypes)

# Tamanho da memoria utilizada
print('Valor de Byte na coluna LojaId com tipo int64')
print(df['LojaID'].memory_usage(deep=True))

# alterar o tipo de dado da colina LojaId
df['LojaID'] = df['LojaID'].astype('object')

# verificar os tipos de dados das colunas
print(df.dtypes)

# Tamanho da memoria utilizada
print('Valor de Byte na coluna LojaId com tipo object')
print(df['LojaID'].memory_usage(deep=True))

print(df.head())

# verificar se existe valores faltantes ou nulos
print(df.isnull().sum())

media_de_vendas = df['Vendas'].mean()
print(media_de_vendas)

# para substituir valores nulos pela média
df['Vendas'].fillna(media_de_vendas, inplace=True)
# outra forma de fazer
df['Vendas'] = df['Vendas'].fillna(media_de_vendas)
# outra forma de fazer
df.loc[:, 'Vendas'].fillna(media_de_vendas, inplace=True)

# para substituir valores nulos por zero
df['Vendas'].fillna(0, inplace=True)
# outra forma de fazer
df['Vendas'] = df['Vendas'].fillna(0)
# outra forma de fazer
df.loc[:, 'Vendas'].fillna(0, inplace=True)

# apagar linha com valores nulos
df.dropna(inplace=True)

# apagar linha com valores nulos com base apenas em uma coluna
df.dropna(subset=['Vendas'], inplace=True)

# removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how='all', inplace=True)

print(df.head())
# procurando valores em uma determinada coluna
valor_procurado = 3.01
print(df.loc[df['Vendas'] == valor_procurado])

# Criando nova coluna receita
df['Receita'] = df['Vendas'].mul(df['Qtde'])

print(df.head())

# Criando nova qtd
df['Qtde_2'] = df['Receita'] / df['Vendas']
df['Qtde_2'] = df['Qtde_2'].astype(int)

print(df.head())

# retornando maior receita
print(df['Receita'].max())

# as linhas Top 3 com maior receita
print(df.nlargest(3, 'Receita'))

# retornando menor receita
print(df['Receita'].min())

# as linhas top 3 com menor receita
print(df.nsmallest(3, 'Receita'))

# agrupamento de receita por cidade
print(df.groupby('Cidade')['Receita'].sum())

# ordenar conjunto de dados
print(df.sort_values('Receita', ascending=False).head(10))
