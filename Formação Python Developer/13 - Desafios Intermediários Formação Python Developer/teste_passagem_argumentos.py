saldo = 100
deposito = 50
saque = 50


def teste_deposito(saldo_, deposito):
    valor = saldo_ + deposito
    global saldo
    saldo += valor
    return saldo


teste_deposito(saldo, deposito)

print(saldo)


def teste_saque():
    pass
