def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def exibir_resultado(a, b, funcao):

    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}.')


exibir_resultado(10, 10, soma)
exibir_resultado(10, 10, subtracao)

op = soma(1, 2)
print(op)
