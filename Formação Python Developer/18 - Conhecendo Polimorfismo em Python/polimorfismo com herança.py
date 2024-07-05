# na herança a classe filha herda os métodos da classe pai.
# no entanto é possível modificar um método em uma classe filha
# herdade da classe pai.

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando...')


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
