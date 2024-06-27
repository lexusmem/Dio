cores = ['preto', 'azul', 'vermelho', 'rosa', 'azul', 'terra', 'a', 'as']

# função built in sorted
# sorted tem que ser informado os argumentos
print(sorted(cores))
print(sorted(cores, key=lambda x: len(x)))
print(sorted(cores, key=lambda x: len(x), reverse=True))
