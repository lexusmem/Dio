''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 

N = int(input())

while(n > 0):

    Todo  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.

'''

'''
Exemplo de Entrada	Exemplo de Saída
4
56234523485723854755454545478690 78690 - encaixa
5434554 543 - nao encaixa
1243 1243 - encaixa
54 64545454545454545454545454545454554 - nao encaixa
'''

# a = 56234523485723854755454545478690
# a_string = str(a)
# tamanho_a = len(a_string)
# b = 78690
# b_string = str(b)
# tamanho_b = len(b_string)
# print(a_string[-tamanho_b:])
# print(b_string)
# print(a_string[-tamanho_b:] == b_string)

N = int(input())


while (N > 0):
    A, B = input().split()
    if B < A:
        print('nao encaixa')
        N -= 1
        continue

    a_string = str(A)
    tamanho_a = len(a_string)
    b_string = str(B)
    tamanho_b = len(b_string)

    if (a_string[-tamanho_b:]) == b_string:
        print('encaixa')
    else:
        print('nao encaixa')

    N -= 1
