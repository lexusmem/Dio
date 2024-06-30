# método construtor - utilizado quando inicializado uma classe
# método inicializador

# __init__ - método especial.

# método destrutor - utilizado quando instancia da classe é destruída
# python possui um coletor de lixo automático
# __del__

from functools import cache
from shlex import join


class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando instância....')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Destruindo a instância....')

    def falar(self):
        print('Auau')


def criar_cachorro():
    c = Cachorro('Zeus', 'Preto', False)
    print(c.nome)


criar_cachorro()

c = Cachorro('Chapie', 'Amarelo')
c.falar()

print('teste')
print('Forçando a destrição do objeto:')
del c
print('teste')
print('teste')
