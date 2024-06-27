cores = ['preto', 'azul', 'vermelho', 'rosa', 'azul', 'terra', 'a', 'as']

cores.sort()
print(cores)

cores.sort(reverse=True)
print(cores)

cores.sort(key=lambda x: len(x))
print(cores)

cores.sort(key=lambda x: len(x), reverse=True)
print(cores)
