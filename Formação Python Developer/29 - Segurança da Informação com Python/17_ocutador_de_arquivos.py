import ctypes
import os

atributos_ocutar = 0x02

caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\29 - Segurança da Informação com Python'

name_arquivo = input('Informe o nome do arquivo para ocultar: ')

arquivo = os.path.join(caminho, name_arquivo)

# Caminho do arquivo para validar se esta correto:
# print(arquivo)

# Verificar se o arquivo está oculto
# -1 arquivo não localizado
# 2 arquivo oculto
# 32 arquivo não oculto
atributos_atuais = ctypes.windll.kernel32.GetFileAttributesW(arquivo)

if atributos_atuais == -1:
    print('Arquivo não Localizado.')
    exit()
elif atributos_atuais == 2:
    print('Arquivo já Oculto')
    question = input('Deseja desocultar o arquivo? S(Sim) ou N(Não): ')
    if question == 'S':
        novos_atributos = atributos_atuais & ~atributos_ocutar
        retorno = ctypes.windll.kernel32.SetFileAttributesW(
            arquivo, novos_atributos)
        print('Arquivo Desocultado!')
        exit()
    else:
        exit()

retorno = ctypes.windll.kernel32.SetFileAttributesW(
    arquivo, atributos_ocutar)

if retorno:
    print('Arquivo Ocultado')
