# métodos de classe
# estão ligados a classe e não ao objeto
# tem acesso ao estado da classe
# não chama a classe chama ao obj
# criar métodos de fabrica


# métodos estáticos
# não recebe o primeiro parâmetro explicito
# tb é um objeto ligado a classe e não ao objetos
# não altera o estado da classe
# criar funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod  # METODO DE CLASSE
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # por convensão no lugar do self utiliza cls
        # print(cls)
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod  # MÉTODO Estáticos
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa('Alex', 37)
# print(p.nome, p.idade)


p = Pessoa.criar_de_data_nascimento(1987, 1, 19, 'Alex')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))
