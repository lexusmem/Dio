import pandas as pd
import os

caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\30 - Análise de dados com Python e Pandas\datasets'

arquivo = 'Gapminder.csv'

arquivo_utilizar = os.path.join(caminho, arquivo)

# data frame - conjunto de dados
df = pd.read_csv(arquivo_utilizar, on_bad_lines='skip', sep=';')

# vizualizando as 5 primeiras linhas
print(df.head())

# alterando os nomes das colunas
# por padrão eu deveria criar um no df( df = df.rename(...))
# porém posso utilizar o argumento inplace=true dentro do método .rename().
# Isso fará com que o método modifique o DataFrame original diretamente,
# sem a necessidade de reatribuição:
df.rename(columns={'country': 'Pais', 'continent': 'Continente', 'year': 'Anos',
          'lifeExp': 'Exp de Vida', 'pop': 'Populacao', 'gdpPercap': 'PIB'}, inplace=True)


# vizualizando as 5 primeiras linhas
print(df.head(10))

# total de linhas e colunas
print(df.shape)

# retornar as colunas
print(df.columns)
print(list(df.columns))

# tipo de dados de cada coluna
print(df.dtypes)

# vizualizar as ultimas linhas do df
print(df.tail())

# descrição do conjunto de dados
print(df.describe())

# retornar valores de uma coluna
print(df['Continente'])

# retornar valores de uma coluna com dados únicos
print(df['Continente'].unique())

# filtros

# filtrando coluna continente onde consta oceania
oceania = df.loc[df['Continente'] == 'Oceania']
print(oceania.head())

# retornando os paises que constam no continente oceania
paises_oceania = oceania['Pais'].unique()
print(paises_oceania)

dados_fiji = df.loc[df['Pais'] == 'Fiji']
print(dados_fiji)

paises_america = df.loc[df['Continente'] == 'Americas']['Pais'].unique()
print(paises_america)

dados_brazil = df.loc[df['Pais'] == 'Brazil']
print(dados_brazil)

# agrupamento de dados
# agrupamento por continente
# contagem de pais exclusivos nos continentes
qtd_paises = df.groupby('Continente')['Pais'].nunique()
print(qtd_paises)

qtd_anos = df.groupby('Pais')['Anos'].nunique()
print(qtd_anos)
print(qtd_anos['Brazil'])
print(qtd_anos.loc['Brazil'])

# para cada ano, qual a expectativa de vida
exp_por_ano = df.groupby('Anos')['Exp de Vida'].mean()
print(exp_por_ano)

# media da coluna
media_pib = df['PIB'].mean()
print(media_pib)

# soma da coluna pib
soma_pib = df['PIB'].sum()
print(soma_pib)
