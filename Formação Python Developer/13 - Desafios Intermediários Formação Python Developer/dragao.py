def nivel_energia(valor):
    if valor <= 8000:
        return 'Inseto!'
    else:
        return 'Mais de 8000!'


C = int(input())
for i in range(C):
    valor = int(input())
    print(nivel_energia(valor))
