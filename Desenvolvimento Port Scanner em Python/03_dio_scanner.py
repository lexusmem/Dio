import nmap

scanner = nmap.PortScanner()


# função para verificar se é numero
def eh_numero(digito):
    return digito.isdigit()


# Função do Menu
def menu():
    return input('''
Escolha o tipo de varredura a ser realizada
1 - Varredura do Tipo SYN
2 - Varredura do Tipo UDP
3 - Varredura do Tipo Intensa
                       
Digite a opção escolhida: ''')


print('Seja Bem Vindo ao LEXUS Scanner.\n')

ip = input('Digite o I.P. e/ou Host a ser analisado: ')
print(f'\nO ip/host informado foi {ip}.')

tipo_varredura = menu()

while not eh_numero(tipo_varredura):
    print('Digite apenas números.')
    tipo_varredura = menu()

while int(tipo_varredura) < 1 or int(tipo_varredura) > 3:
    print('Digite apenas números de 1 a 3.')
    tipo_varredura = menu()

print(f'A Varredura selecionada foi do tipo {tipo_varredura}.')
print('Iniciando Varredura...')

if tipo_varredura == '1':
    print(f'Versão do Nmap: {scanner.nmap_version()}')
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(f'Status do IP/Host: {scanner[ip].state()}.')
    print(scanner[ip].all_protocols())
    print(f'Portas Abertas: {scanner[ip]['tcp'].keys()}')
elif tipo_varredura == '2':
    print(f'Versão do Nmap: {scanner.nmap_version()}')
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(f'Status do IP/Host: {scanner[ip].state()}.')
    print(scanner[ip].all_protocols())
    print(f'Portas Abertas: {scanner[ip]['udp'].keys()}')
else:
    print(f'Versão do Nmap: {scanner.nmap_version()}')
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print(f'Status do IP/Host: {scanner[ip].state()}.')
    print(scanner[ip].all_protocols())
    print(f'Portas Abertas: {scanner[ip]['tcp'].keys()}')
