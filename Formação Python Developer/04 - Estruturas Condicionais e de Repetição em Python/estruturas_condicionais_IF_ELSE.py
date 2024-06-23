#  estruturas condicionais
# permite desvio de fluxo de controle
# quando atende determinadas expressões lógicas

# if / if-else / elif

saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

#  if e else!!!
if saldo >= saque:
    print('Saque realizado!')
    saldo -= saque
else:
    print('Saldo insuficiente.')
