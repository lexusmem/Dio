# is sub set, verifica se os elementos de um set esta contido em outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

a_pertence_b = conjunto_a.issuperset(conjunto_b)
b_pertence_a = conjunto_b.issuperset(conjunto_a)

print(a_pertence_b)
print(b_pertence_a)
