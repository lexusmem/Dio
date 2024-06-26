menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

saldo = 0.00
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação inválida! Informe um valor válido para deposito.')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo Insuficiente!')
        elif excedeu_limite:
            print('Valor acima do limite de saque!')
        elif excedeu_saques:
            print('Número de Saques diários excedidos!')

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque: R$ {valor:.2f}\n'

        else:
            print('Operação inválida! Informe um valor válido para saque.')

    elif opcao == 'e':
        print('\n========================== EXTRATO ==========================')
        print('Não foram realizados movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('============================================================')

    elif opcao == 'q':
        break

    else:
        print('Operação Inválida, por favor selecione novamente a operação desejada.')
