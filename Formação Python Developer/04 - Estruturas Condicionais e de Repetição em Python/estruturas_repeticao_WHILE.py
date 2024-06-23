# WHILE
# repetir um bloco de código varias vezes
# usar quando não sabemos o número de vezes que deve repetir.

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar [2] Extrato [0] Sair: '))
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Extrato...')

# While pode conter else para ser executado no final da repetição

opcao1 = -1
while opcao1 != 0:
    opcao1 = int(input('[1] Sacar [2] Extrato [0] Sair: '))
    if opcao1 == 1:
        print('Sacando...')
    elif opcao1 == 2:
        print('Extrato...')
else:
    print('Fim do bloco While.')
