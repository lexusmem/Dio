curso = 'pYthon'
# maiusculo
print(curso.upper())
# minusculo
print(curso.lower())
# Primeiro maisculo
print(curso.title())

curso = '         pYthon                 '
# remover espaço da esquerda e da direita
print(curso.strip()+".")
# remover espaço da esquerda
print(curso.lstrip()+".")
# remover espaço da direita
print(curso.rstrip()+".")

curso = 'pYthon'
# unir e centralizar
print(curso.center(10, '#'))
print(curso.center(10))
# Juntar caractere na string
# join funciona em todos os tipos de iteráveis
# vai passar item a item e unir o carácter inserido
print("-".join(curso))
