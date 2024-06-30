# Herança Simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando Motor...')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} estou carregado.')


moto = Motocicleta('Branca', 'ABC1234', 2)
carro = Carro('Branco', 'ASD1478', 4)
caminhao = Caminhao('Gelo', 'FRE1455', 8, True)

print(moto)
moto.ligar_motor()

print(carro)
carro.ligar_motor()

print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
