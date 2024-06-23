# estruturas de repetição - for e while
# repetir um trecho de um código por um determinado número de vezes.

# for - quando sabemos o números de vezes para alteração

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print("")
# FOR ELSE
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("")
    print('Acabou o Else')
