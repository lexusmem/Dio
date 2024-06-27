numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# list comprehension 1
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)

carros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for carro in carros:
    quadrado.append(carro ** 2)
print(quadrado)

# list comprehension 2
quadrado2 = [numero ** 2 for numero in carros]
print(quadrado2)

# list comprehension 3
print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

# Explicação - primeira parte
# n for n in range(10) if n % 2 == 0]
for n in range(10):
    if n % 2 == 0:
        print(n)
# Explicação - segunda parte
# se n > 6 então multiplica pelo quadrado.
