from abc import ABC, abstractmethod
# classes abstratas
# o python não fornece classes abstratas
# para isso utilizamos o modulo ABC


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV...')
        print('Ligado')

    def desligar(self):
        print('Desligando TV...')
        print('Desligado')

    @property
    def marca(self):
        return 'Philco'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando Ar Condicionado...')
        print('Ligado')

    def desligar(self):
        print('Desligando Ar Condicionado...')
        print('Desligado')

    @property
    def marca(self):
        return 'LG'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca())

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca())
