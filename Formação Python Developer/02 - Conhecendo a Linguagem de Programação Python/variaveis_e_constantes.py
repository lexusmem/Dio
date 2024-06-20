# variáveis
# espaço de memoria que recebe valores
# que pode sofrer alterações no decorrer da execução (mutável)

age = 37
name = 'alex'
age, name = (37, 'Alex')
print(f'meu nome é {name} tenho {age} anos.')

# alteração de valores, basta atribuir novos valores
age, name = 38, 'Alex Sousa'
print(f'meu nome é {name} tenho {age} anos.')

# constantes
# espaço de memoria que recebe valores
# os valores são imutáveis não sofre alteração no decorrer do programa

# python não possui constantes
# usamos a convenção que diz que a variável é uma constante
# para constante utiliza a variável em maiúsculo

CONSTANTE = True

# boas praticas
# não ter espaço nos nomes das variáveis utilizar underscore
# escolher nomes sugestivos
# nome de constantes todo em maiúsculo
limite_saque_diario = 1000.00
