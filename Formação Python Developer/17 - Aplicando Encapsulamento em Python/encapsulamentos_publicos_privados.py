# em python não possui palavras reservadas para definir
# o nível de acesso aos atributos e métodos da classe.
# usa-se convenções no nome do recuso, para definir se a
# variável é pública ou privada.

# utilizar o underline no atributo

# publico pode ser acessado de fora da classe
# privado so pode ser acesso pela classe

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return f'{self._saldo:.2f}'


conta = Conta('0001', 100)
conta.depositar(500)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
