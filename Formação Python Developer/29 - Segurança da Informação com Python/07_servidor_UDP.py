import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\nServidor: Olá cliente, ok?!'

while 1:
    dados, endereco = s.recvfrom(4096)
    print(f'Dados Recebido do Cliente: {dados}')
    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), endereco)
