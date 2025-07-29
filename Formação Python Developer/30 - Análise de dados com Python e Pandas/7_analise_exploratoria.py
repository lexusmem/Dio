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

print('\n###### Nome Das Colunas Utilizando Pprint ######')
name_columns = list(df.columns)
pprint.pprint(name_columns)

print('\n###### Nome Das Colunas Utilizando "For" ######')
for name in name_columns:
    print(name)

# valor total das vendas - valor total da receita
valor_total_venda = df['Valor Venda'].sum()

print('\n###### Dados formatados com a biblioteca Babel.numbers ######')
print(format_decimal(valor_total_venda, format='#,##0.00', locale='pt_BR'))
print(format_compact_decimal(valor_total_venda,
      format_type='short', fraction_digits=2))
print(format_compact_decimal(valor_total_venda,
      format_type='long', locale='pt_BR', fraction_digits=2))
print(format_currency(valor_total_venda, 'BRL', locale='pt_BR'))
tipo_valor = format_currency(valor_total_venda, 'BRL', locale='pt_BR')
print(type(tipo_valor))


def imprimir_valor(valor):
    numero = format_decimal(valor, format='#,##0.00', locale='pt_BR')
    return print(numero)


print(round(df['Valor Venda'].sum(), 2))

print('\n###### Valor total da Venda/Receita Total ######')
imprimir_valor(valor_total_venda)


print('\n###### Nova coluna valor total do custo ######')
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
print(df.head(1))

print('\n###### Valor Custo Total ######')
custo_total = df['Custo'].sum()
imprimir_valor(custo_total)


print('\n###### Valor do Lucro ######')
df['Lucro'] = df['Valor Venda'] - df['Custo']
print(df.head(1))

print('\n###### Valor Lucro Total ######')
lucro_total = df['Lucro'].sum()
imprimir_valor(lucro_total)


print('\n###### Tempo de Envio ######')
df['Tempo de Envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
print(df.head(1))
print(df['Tempo de Envio'].dtypes)

print('\n###### Média de dias de Envio por Marca ######')
media_de_envio_marca = df.groupby('Marca')['Tempo de Envio'].mean()
print(media_de_envio_marca)

print('\n###### Verificando se tem valores ausentes ######')
print(df.isnull().sum())

# função panda pra impressão dos números com ponto e virgula
pd.options.display.float_format = '{:20,.2f}'.format

print('\n###### Lucro por Ano e Por Marca ######')
lucro_ano_marca = df.groupby([df['Data Venda'].dt.year, 'Marca'])[
    'Lucro'].sum()
print(lucro_ano_marca)

print('\n###### Novo df lucro por marca Resetanto o Index ######')
lucro_ano = lucro_ano_marca.reset_index()
print(lucro_ano)

print('\n###### Total de produtos Vendidos ######')
produtos_vendidos = df.groupby(
    'Produto')['Quantidade'].sum().sort_values(ascending=False)
print(produtos_vendidos)

print('\n###### Gráfico Total de produtos Vendidos ######')
plot_total_product = df.groupby('Produto')['Quantidade'].sum().sort_values(
    ascending=True).plot.barh(title='Total de Produtos Vendidos')
plt.xlabel('Total')
plt.ylabel('Produto')
plt.show()

print('\n###### Gráfico Total Lucro Por Ano ######')
plt_lucro_ano = df.groupby(df['Data Venda'].dt.year)[
    'Lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.show()

print('\n###### Total Lucro Por Ano ######')
print(df.groupby(df['Data Venda'].dt.year)['Lucro'].sum())

print('\n###### Vendas do Ano de 2009 ######')
df_2009 = df[df['Data Venda'].dt.year == 2009]
print(df_2009.head(10))


print('\n###### Vendas por Meses de 2009 ######')
print(df.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum())


print('\n###### Gráfico Lucro x Mês 2009 ######')
df_2009.groupby(df_2009['Data Venda'].dt.month)[
    'Lucro'].sum().plot(title='Lucro x Mês 2009')
plt.xlabel('Mês')
plt.ylabel('Receita')
plt.show()

print('\n###### Lucro x Marca - 2009 ######')
print(df_2009.groupby('Marca')['Lucro'].sum())


print('\n###### Gráfico Lucro x Marca - 2009 ######')
df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title='Lucro x Marca 2009')
plt.xlabel('Marca')
plt.ylabel('Receita')
plt.show()

print('\n###### Lucro x Classe - 2009 ######')
print(df[df['Data Venda'].dt.year == 2009].groupby('Classe')['Lucro'].sum())
print(df_2009.groupby('Classe')['Lucro'].sum())


print('\n###### Gráfico Lucro x Classe - 2009 ######')
df_2009.groupby('Classe')['Lucro'].sum().plot.bar(
    title='Lucro x Classe - 2009')
plt.xlabel('Classe')
plt.ylabel('Receita')
plt.xticks(rotation='horizontal')
plt.show()

print('\n###### Classe Describe - Tempo de Envio ######')
print(df['Tempo de Envio'].describe())

print('\n###### Gráfico de Boxplort - Tempo de Envio ######')
plt.boxplot(df['Tempo de Envio'])
plt.show()

print('\n###### Gráfico de Histograma - Tempo de Envio ######')
plt.hist(df['Tempo de Envio'])
plt.show()

print('\n###### Tempo Mínimo de Envio ######')
print(df['Tempo de Envio'].min())

print('\n###### Tempo Máximo de Envio ######')
print(df['Tempo de Envio'].max())

print('\n###### Identificar Outlier ######')
print(df[df['Tempo de Envio'] == 20])

print('\n###### Identificar Mínimo ######')
print(df[df['Tempo de Envio'] == 4])

print('\n###### Salvar Arquivo ######')
arq_salvo = os.path.join(caminho, 'df_vendas_novo_df.csv')
df.to_csv(arq_salvo, index=False)
print('Arquivo Criado e Salvo!')
