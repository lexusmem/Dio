# ler valores com função builtin input
# recebe string
nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')

# exibir valor função print
# 4 argumentos opcionais (sep, end, file e flush)

print(nome, sobrenome)
print(nome, sobrenome, end='...\n')
print(nome, sobrenome, sep='#')
print(nome, sobrenome, sep='#', end='...\n')
