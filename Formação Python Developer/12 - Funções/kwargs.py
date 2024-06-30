lista = {'nome': 'alex', 'tipo': 'teste',
         'numero': 1, 'numero2': 2, 'bool': True}


def teste(**kwargs):
    for chave, elementos in kwargs.items():
        print(chave, elementos)


print(lista['nome'])
nexttt = next(iter(lista.items()))
print(nexttt)
teste(**lista)
