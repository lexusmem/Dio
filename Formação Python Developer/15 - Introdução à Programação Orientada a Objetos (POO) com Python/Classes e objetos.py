# CLASSES
# define característica e comportamento de um objeto
# algo abstrato
# não conseguimos utiliza-las diretamente

# OBJETOS
# podemos usa-los
# eles possuem as características e comportamentos definidos nas classes
# ao instancia-los podemos utiliza-los

# classe é a estrutura de um objeto (uma planta de uma casa)
# a classe diz como o objeto vai ser, o que vai possuir (objeto é a classe construida com a planta)

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        if self.acordado == True:
            print('Auau')
        else:
            print("Eu estou dormindo!")

    def dormir(self):
        self.acordado == False
        print('Zzzzzz....')


cao_1 = Cachorro('Chapie', 'Marron', False)
cao_2 = Cachorro('Tooper', 'Preto')

cao_2.latir()
cao_1.latir()
print(cao_2.acordado)
print(cao_1.acordado)
cao_2.dormir()
print(cao_2.acordado)
