#  estruturas condicionais
# permite desvio de fluxo de controle
# quando atende determinadas expressões lógicas

# if / if-else / elif

saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

#  vários if!!!
if saldo >= saque:
    print('Saque realizado!')
    saldo -= saque

if saldo < saque:
    print('Saldo insuficiente.')
