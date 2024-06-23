#  estruturas condicionais
# permite desvio de fluxo de controle
# quando atende determinadas expressões lógicas

# if / if-else / elif

saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

# if Aninhados
opcao = int(input("Informe sua opção: [1] Sacar [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    if saldo >= saque:
        print('Saque realizado!')
        saldo -= saque
    else:
        print('Saldo insuficiente.')
elif opcao == 2:
    print(f'Seu saldo é de R$ {saldo}.')
else:
    print('Opção não disponível.')
