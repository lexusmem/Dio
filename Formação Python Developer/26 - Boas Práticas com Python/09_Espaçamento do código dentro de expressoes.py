# deve existir espaços entre os elementos da função/lista/parametro

def media_aluno(nota1, nota2, divisor):
    calculo = (nota1/nota2)/divisor
    return calculo


alex = media_aluno(1, 2, 5)


def funcao_ficticia(*args):
    print(args[0])
    print(args[1])


vetor = [0, 2, 3]

funcao_ficticia(vetor, {'key': 2})

# mais sobre estações

foo = (0,)  # correto
bar = (0, )  # errado
