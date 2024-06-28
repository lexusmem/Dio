# difference - tudo que são diferentes no primeiro conjunto em relação ao segundo

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

dif_de_a_com_b = conjunto_a.difference(conjunto_b)
dif_de_b_com_a = conjunto_b.difference(conjunto_a)

print(dif_de_a_com_b)
# {1}
print(dif_de_b_com_a)
# {4}
