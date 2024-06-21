# identação é a forma de mater o código fonte mais legível e manutenível
# em python a identação determina onde um bloco inicia e termina

# bloco de comandos
# convenção para digitação de código
# 4 espaços em branco em nível de identação

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print(f'Valor sacado {valor}')
        saldo -= valor
    else:
        print(f'Não possui saldo. Seu saldo é de {saldo}')
    # fim do bloco if
# fim do método


def depositar(valor):
    saldo = 500
    saldo += valor
    return saldo


sacar(500)
sacar(600)

print(depositar(200))
