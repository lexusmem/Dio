# * args - tupla
# ** kwargs - dicionario
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join(
        [f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)


exibir_poema('Sexta-Feira 28 Junho de 2022', 'Zen of Python', 'Beatiful is better than uggly.',
             'Teste *args: Listas', autor='Tim Peters', ano=1999, teste='**kwargs - Dicionario Chave e Valor')
