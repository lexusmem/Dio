'''
Criando consulta de ping simples com python.
'''
import os  # importa a biblioteca os
# (integra os programas e recursos do sistema operacional)

ip_ou_host = input('Digite o IP ou host a ser verificar: ')

num_de_consultas = input('Digite um número de consultas: ')

os.system(f'ping -n {num_de_consultas} {ip_ou_host}')
