class Estudante:
    escola = 'dio'  # ATRIBUTO DE CLASSE únicas para todos objetos

    def __init__(self, nome, matricula):  # self é a instancia
        self.nome = nome  # VARIÁVEL DE INSTANCIA
        self.matricula = matricula  # VARIÁVEL DE INSTANCIA

    def __str__(self):
        return f'nome: {self.nome} - Matricula: {self.matricula} - Escola: {self.escola}.'


def mostrar_aluno(*objeto):
    for obj in objeto:
        print(obj)


aluno1 = Estudante('Alex', 1)
aluno2 = Estudante('Sabrina', 2)

mostrar_aluno(aluno1, aluno2)
Estudante.escola = 'Python'

aluno3 = Estudante('Cynthia', 3)
mostrar_aluno(aluno1, aluno2, aluno3)

aluno1.escola = 'DIO'
mostrar_aluno(aluno1, aluno2, aluno3)
