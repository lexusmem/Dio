# Nomeação explicitada das funções
# função minusculas
# classe primeira maiúscula e demais minusculas

def print_hi(name):
    # Use breakpoint in the code line below to debug your script
    print(f'Hi, {name}')  # Press crtl+f8 to toogle the breakpoint


class Person:
    def __init__(self, message):
        # self primeiro argumento
        self.inicio = message
    pass


if __name__ == '__main__':
    print_hi('Alex Sousa')
