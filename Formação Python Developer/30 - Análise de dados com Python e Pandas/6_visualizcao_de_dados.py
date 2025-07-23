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

# gráfico de barras vertical
# df['LojaID'].value_counts(ascending=False).plot.bar()
# plt.show()

# grafico barras horizontais
# df['LojaID'].value_counts(ascending=True).plot.barh()
# plt.show()  # apresentando o gráfico

# gráfico pizza
# df.groupby(df['Ano_Venda'])['Receita'].sum().plot.pie()
# plt.show()

print(df['Cidade'].value_counts())

# adicionando um titulo e alterando o nome dos eixos
# x - eixo horizonte
# y - eixo vertical
# df['Cidade'].value_counts().plot.bar(title='Total Vendas por Cidade')
# plt.xlabel('Cidade')
# plt.ylabel('Total Vendas')
# plt.show()

# Alterar a cor do gráfico
# df['Cidade'].value_counts().plot.bar(
#     title='Total Vendas por Cidade', color='gray')
# plt.xlabel('Cidade')
# plt.ylabel('Total Vendas')
# plt.show()

# alterar estilo dos graficos
plt.style.use('ggplot')

# grafico com valor total de venda por mes.
df.groupby(df['Mes_venda'])['Qtde'].sum().plot(title='Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend()
plt.show()

# somarização de vendas por mês
print(df.groupby(df['Mes_venda'])['Qtde'].sum())

# criação de df com dados das vendas do ano de 2019
df_19 = df.loc[df['Ano_Venda'] == 2019]

# somarização de vendas de 2019 por mês
print(df_19.groupby(df_19['Mes_venda'])['Qtde'].sum())

# gráfico com valor total de venda do ano de 2019 por mês.
df_19.groupby(df_19['Mes_venda'])['Qtde'].sum().plot(
    marker='o', title='Vendas por mês ano 2019')
plt.xlabel('Mês Venda')
plt.ylabel('Qtde de Vendas')
plt.legend()
plt.show()

# gráfico de histrograma
plt.hist(df['Qtde'], color='dimgray')
plt.show()

# gráfico de dispersão
plt.scatter(x=df_19['Dia_venda'], y=df_19['Receita'])
plt.show()

# salvando as imagens em png
nome_arquivo = 'grafico_dispersao.png'
salvar_imagem = os.path.join(caminho, nome_arquivo)
plt.scatter(x=df_19['Dia_venda'], y=df_19['Receita'])
plt.savefig(salvar_imagem, dpi=300)
