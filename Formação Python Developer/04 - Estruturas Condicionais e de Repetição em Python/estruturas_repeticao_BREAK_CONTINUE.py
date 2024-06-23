opcao = -1

# função break - para laço de repetição for or while
while True:
    opcao = int(input('Informe um número: '))
    if opcao == 10:
        break
    print(f'Número informado {opcao}')

# função continue - pula uma execução
for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=" ")

print("")
# números ímpares
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")

print("")
# números pares
for numero in range(100):
    if numero % 2 == 1:
        continue
    print(numero, end=" ")
