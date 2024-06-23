#  estruturas condicionais
# permite desvio de fluxo de controle
# quando atende determinadas expressões lógicas

# if / if-else / elif

saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

# if Ternário
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar o saque.')
