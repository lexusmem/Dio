import socket

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.settimeout(0.05)

ip = input('Informe o host ou ip para verificar: ')
port = int(input('Digite a porta a ser verificada: '))

code = CLIENT.connect_ex((ip, port))

if code == 0:
    print('Porta Aberta.')
    print(f'Retorno da conexão n° {code}.')
else:
    print('Porta Fechada.')
    print(f'Retorno da conexão n° {code}.')
