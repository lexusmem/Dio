# é um bloco de código com um identificador
# que pode receber parâmetros para ser utilizado no
# trecho de código da função
# e que pode possuir ou não um retorno

# funções - programar de maneira estruturado

def exibir_mensagem():
    print('Olá mundo!')


def exibir_mensagem2(nome):
    print(f'Seja bem vindo {nome}.')


def exibir_mensagem3(nome='Alex'):
    print(f'Seja bem vindo {nome}.')


exibir_mensagem()
exibir_mensagem2(nome='Alex')
exibir_mensagem3()
exibir_mensagem3(nome='Alex_teste')
