import socket


# função para verificar se é numero
def eh_numero(digito):
    return digito.isdigit()


ip = input('Informe o host ou ip para verificar: ')

n_portas_analise = 0
ports = []
count = 0

n_portas_analise = input('Informe o número de portas a ser analisada: ')

while not eh_numero(n_portas_analise):
    print('Digite apenas números')
    n_portas_analise = input('Informe o número de portas a ser analisada: ')

while count < int(n_portas_analise):
    num_porta = input('Digite a porta a ser verificada: ')
    if eh_numero(num_porta):
        ports.append(num_porta)
        count += 1
    else:
        print('Digite apenas números.')
        continue

for port in ports:
    porta = int(port)
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.settimeout(0.05)
    code = CLIENT.connect_ex((ip, porta))

    if code == 0:
        print(f'Porta n° {str(porta)} Aberta.')
        print(f'Retorno da conexão n° {code}.\n')
    else:
        print(f'Porta n° {str(porta)} Fechada.')
        print(f'Retorno da conexão n° {code}.\n')

print('Scan Finalizado')
