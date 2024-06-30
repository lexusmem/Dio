lista = ('alex', 'teste', 1, 2, True)


def teste(*args):
    for elementos in args:
        print(elementos)


teste(*lista)

teste('alex', 2, 'teste', True)
