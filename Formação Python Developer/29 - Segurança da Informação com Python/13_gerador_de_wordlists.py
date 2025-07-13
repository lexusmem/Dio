import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))

contagem = 1

for caracter in resultado:
    print(contagem, end=' - ')
    print(''.join(caracter))
    contagem += 1
