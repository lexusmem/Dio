# Nomeação explicitada das funções
# função minusculas
# variáveis minusculas - espaços entre as atribuições
# utilizar underline para separar
# classe primeira maiúscula e demais minusculas
# Quando duas palavras na nomeação não separa por underline
# apenas a proxima palavra maiuscula
# -Pessoa
# PessoaJuridica
# Constantes é nomeada Maiúscula

CONSTANTE = 3.80738


def print_hi(name):
    # Use breakpoint in the code line below to debug your script
    print(f'Hi, {name}')  # Press crtl+f8 to toogle the breakpoint


class Person:
    def __init__(self, message):
        # self primeiro argumento
        self.name = None
        self.inicio = message
    pass

    def set_name(self, name):
        self.name = name
        print('O nome é:', name)


# função composta
def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four):
    pass


if __name__ == '__main__':
    print_hi('Alex Sousa')
