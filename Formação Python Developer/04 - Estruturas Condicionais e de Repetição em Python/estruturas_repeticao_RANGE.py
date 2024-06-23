# range
# produzir sequencia de número inteiros
# inicio inclusivo e fim exclusivo

# range(stop)
print(range(4))
print(list(range(4)))


# range(start, stop, step)
# range com for
for numero in range(0, 11):
    print(numero, end=" ")

print("")
# exibindo tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
