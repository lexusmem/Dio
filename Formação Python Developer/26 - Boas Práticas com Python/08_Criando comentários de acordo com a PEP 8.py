'''
# docstring: escrito dentro das
'''

# Comentários no código
'''
* Comentários tanto quanto necessário
* Objetivo: facilitar o entendimento
* Código bem escrito também é documentado
'''


class Person:
    def __init__(self, message, nome):
        # self primeiro argumento
        self.nome = nome
        self.inicio = message
    pass

    def set_name(self, name):
        '''
            Este método tem por objetivo setar o nome do
        objeto instanciado na classe.

        :param nome: o nome definido pelo usuário
        :return: retorna um nome via print
        '''
        self.name = name
        print('O nome é:', name)
