import socket
# relacionamento da placa de rede com sistema operacional
import sys
# fornece acesso a algumas variáveis e funções que tem
# forte relação com o interpretador python


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso.')

    host_alvo = input('Digite o host ou I.P. a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f'Cliente TCP conectado com sucesso no host "{
              host_alvo}" na portal "{porta_alvo}".')
        s.shutdown(2)
    except socket.error as e:
        print(f'A conexão falhou! Não foi possível conectar no host "{
              host_alvo}" porta "{porta_alvo}".')
        print(f'Erro: {e}.')


if __name__ == '__main__':
    main()
