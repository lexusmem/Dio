# Criando lista
animais = [1, 2, 3]

print(animais)

animais = ['cachorro', 'gato', 12345, 5.8]

print(animais)

# impresão elementos lista
print(animais[0])
print(animais[3])

# substituindo elementos da lista
animais[0] = 'urso'
print(animais)

# remover elemento
animais.remove('urso')
print(animais)

# tamanho lista
print(len(animais))

# pertence?
pertence = 'urso' in animais
print(pertence)
pertence_2 = 'gato' in animais
print(pertence_2)

# maximo e minimo
num = [456, 23, 1, 4566, 4346778, 546743]

print(num)
print(max(num))
print(min(num))

# adicionar na lista
animais.append('leão')
print(animais)

animais.append(['teste', 123])
print(animais)

# adicionar mais de um
animais.extend(['papagaio', 'marsupial'])
print(animais)

# verificar se consta dados na lista
print(animais.count('marsupial'))
print(animais.count(123))

# ordenar
print(num)
num.sort()
print(num)

# tuplas - imultavel

tp = ('banana', 1, 'maça')

print(tp)

print(tp[0])
print(tp[0:2])

# dicionarios

dc = {'maça': 20, 'banana': 10, 'laranja': 15, 'morango': 56}

print(dc)
print(dc['maça'])

dc['maça'] = 25
print(dc['maça'])

print(dc.keys())
print(list(dc.keys()))
print(dc.values())
print(list(dc.values()))

# Verificando se já existe uma chave no dicionário e caso não exista inserir
dc.setdefault("Limão", 22)

print(dc)
