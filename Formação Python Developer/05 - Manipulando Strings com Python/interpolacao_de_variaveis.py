# 3 formas de interpolar
nome = 'alex'
idade = 28
profissao = 'securitario'
linguagem = 'Python'

# % - não recomendado
print('olá me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou \
matriculado no curso de %s.' % (nome, idade, profissao, linguagem))
# s tipos strings
# d tipos inteiros
# b tipos bools

# format
print('olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou \
matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

print('olá me chamo {3}. Eu tenho {0} anos de idade, trabalho como {1} e estou \
matriculado no curso de {2}.'.format(idade, profissao, linguagem, nome))

print('olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou \
matriculado no curso de {linguagem}.'.format(idade=idade, profissao=profissao, linguagem=linguagem, nome=nome))

dados = {'nome': 'alex', 'idade': 37,
         'profissao': 'securitário', 'linguagem': 'Python'}

print('olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou \
matriculado no curso de {linguagem} --- teste dicionário.'.format(**dados))

# f string
print(f'olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como '
      f'{profissao} e estou matriculado no curso de {linguagem}.')

# FORMATAÇÃO
PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')
