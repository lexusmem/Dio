import socket
# relacionamento da placa de rede com sistema operacional

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso.')

host = 'localhost'
porta = 5433
mensagem = 'Ola servidor, tudo certo?'

try:
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}.')
finally:
    print('Cliente: Fechando conexão.')
    s.close()
