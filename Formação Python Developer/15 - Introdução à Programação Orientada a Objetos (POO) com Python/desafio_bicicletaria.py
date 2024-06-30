class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor  # atributos da classe
        self.modelo = modelo  # atributos da classe
        self.ano = ano  # atributos da classe
        self.valor = valor  # atributos da classe
    # self referencia para o objeto, referencia implícita.
    # self representa a instancia do objeto

    # Métodos - é uma função da classe
    # Comportamento das classes
    def buzinar(self):  # Métodos - é uma função da classe
        print('Plim plim...')

    def parar(self):  # Métodos - é uma função da classe
        print('Parando bicicleta...')
        print('Bicicleta Parada!')

    def correr(self):  # Métodos - é uma função da classe
        print('Vrummmm.....')

    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


b1 = Bicicleta('Azul', 'Caloi Ceci', '2024', 750)

b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta('verde', 'monark', 2000, 189)
b2.buzinar()  # Bicicleta.buzinar(b2)
print(b2.cor)

print(b2)
