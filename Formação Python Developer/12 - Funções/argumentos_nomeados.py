def salvar_carro(marca, modelo, ano, placa):
    print(f'carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')


salvar_carro('fiat', 'palio', 1999, 'abc-1234')
salvar_carro(marca='fiat', modelo='palio', ano=1999, placa='abc-1234')
salvar_carro(**{'marca': 'fiat', 'modelo': 'palio',
             'ano': 1999, 'placa': 'abc-1234'})
