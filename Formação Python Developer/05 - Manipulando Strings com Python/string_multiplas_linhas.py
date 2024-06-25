nome = 'Alex'
curso = 'Python'

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo {curso}.
"""
print(mensagem)

# string múltiplas respeita os espaçamentos
mensagem2 = f"""
Olá meu nome é {nome},
      Eu estou aprendendo {curso}.
   Teste!
"""
print(mensagem2)

print('''
    ********MENU**********
    1 - Depositar
    2 - Sacar
    3 - Sair
    **********************
''')
