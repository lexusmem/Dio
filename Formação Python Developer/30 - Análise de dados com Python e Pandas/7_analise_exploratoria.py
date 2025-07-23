import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# plt.style.use('seaborn')
import pprint
# Importe as funções específicas
from babel.numbers import format_decimal, format_currency, format_compact_decimal

caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\30 - Análise de dados com Python e Pandas\datasets'
nome_arquivo = 'AdventureWorks.xlsx'
arquivo = os.path.join(caminho, nome_arquivo)

# criação data frame
df = pd.read_excel(arquivo)
print(df.sample(5))

# linhas e colunas
print(df.shape)

# tipos de dados de cada coluna
print(df.dtypes)

# nome das colunas
name_columns = list(df.columns)

pprint.pprint(name_columns)

for name in name_columns:
    print(name)

valor_total_venda = df['Valor Venda'].sum()
# qual foi a receita total
print(format_decimal(valor_total_venda, format='#,##0.00', locale='pt_BR'))
print(format_compact_decimal(valor_total_venda,
      format_type='short', fraction_digits=2))
print(format_compact_decimal(valor_total_venda,
      format_type='long', locale='pt_BR', fraction_digits=2))
print(format_currency(valor_total_venda, 'BRL', locale='pt_BR'))

# https://web.dio.me/lab/analise-de-dados-com-python-e-pandas/learning/08483f26-f4aa-4b3b-a68f-c6109db6839a
# parei no minuto 5:30min
