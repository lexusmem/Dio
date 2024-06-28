# isdisjoin - todos os elementos não fazem parte do outro conjunto

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {0, 1}

a_nao_esta_b = conjunto_a.isdisjoint(conjunto_b)
c_nao_esta_a = conjunto_c.isdisjoint(conjunto_a)
a_nao_esta_c = conjunto_a.isdisjoint(conjunto_c)

print(a_nao_esta_b)
print(c_nao_esta_a)
print(a_nao_esta_c)
