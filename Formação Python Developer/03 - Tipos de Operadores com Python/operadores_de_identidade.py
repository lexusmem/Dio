# para comparar se dois objetos ocupam a mesma região de memoria


curso = 'alex sousa'
nome_curso = curso

print(curso is nome_curso)
print(curso is not nome_curso)

saldo, limite = 200, 200
print(saldo is limite)

saldo, limite = 200, 100
print(saldo is limite)
