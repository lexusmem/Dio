# dentro do bloco da função é local (restrito ao escopo da função)
# é possivel utilizar uma variavel globla em um ambiente local
# utilizando a palavra reservada 'GLOBAL
# cuidado com listas pois são imutaveis e se alterada no escopo local vai refletir no escopo global
# um jeito é criar lista auxiliar dentro do escopo local

salario = 2000


def salario_bonus(bonus, lista):

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'lista_aux = {lista_aux}')

    global salario
    salario += bonus
    return salario


lista = [1]
salario_bonus(500, lista)
print(salario)
print(lista)
