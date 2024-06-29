'''
Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000), que indica o número de casos de teste.
Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),
respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia,
se aproveitar ao máximo a oferta.
'''

T = int(input())

for i in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    # ou
    # v = input().split(" ")
    # N = int(v[0])
    # K = int(v[1])
    total = int(N % K) + int(N/K)
    print(total)
