# em conjunto com operadores de comparação

saldo = 1000
saque = 200
limite = 100

# operador E
# and
print(saldo >= saque and saque <= limite)

# operador OU
# or
print(saldo >= saque or saque <= limite)

# operador NEGAÇÃO
contatos_emergencia = []

# not
print(not 1000 > 1500)

# lista vazia é falso
print(not contatos_emergencia)

# str é uma sequencia e se estiver vazia é falso em python
print(not "saque 1500")
print(not "")

# parênteses - precedência
conta_especia = True
print((saldo >= saque and saque <= limite)
      or (conta_especia and saldo >= saque))
