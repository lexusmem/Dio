import os
import time

with open(r'c:\Users\lexus\Documents\Estudos\Dio\Formação Python Developer\29 - Segurança da Informação com Python\hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f'Verificando o host: {ip}.')
        os.system(f'ping -n 2 {ip}')
        print('\n')
        time.sleep(5)
