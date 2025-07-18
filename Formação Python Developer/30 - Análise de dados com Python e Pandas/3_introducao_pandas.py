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

# parei no minuto 14:25h
# https://web.dio.me/lab/analise-de-dados-com-python-e-pandas/learning/c14c9169-c62d-4d8a-8ed8-04cbb51d5302
