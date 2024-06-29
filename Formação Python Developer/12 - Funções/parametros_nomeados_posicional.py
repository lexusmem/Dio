# parâmetros nomeados

# '*' parâmetros depois do asteriscos serrão apenas nomeados

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro('Palio', 1999, 'abc-1234', marca='fiat',
            motor='1.0', combustivel='eletrico')  # valido

# criar_carro('Palio', 1999, 'abc-1234', 'fiat', motor='1.0',
#             combustivel='eletrico')  # invalido

# criar_carro('Palio', ano=1999, placa='abc-1234', marca='fiat',
#             motor='1.0', combustivel='eletrico')  # invalido

# criar_carro('Palio', 1999, placa='abc-1234', marca='fiat',
#             motor='1.0', combustivel='eletrico')  # invalido


# criar_carro(modelo='Palio', 1999, 'abc-1234', marca='fiat', motor='1.0', combustivel='eletrico')
