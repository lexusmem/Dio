import hashlib

arquivo1 = r'C:\Users\lexus\Documents\Estudos\Dio\Formação Python Developer\29 - Segurança da Informação com Python\a.txt'
arquivo2 = r'C:\Users\lexus\Documents\Estudos\Dio\Formação Python Developer\29 - Segurança da Informação com Python\b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() == hash2.digest():
    print('Resultado Igual!')
    print(f'Hash do arquivo a.txt é: {hash1.hexdigest()}')
    print(f'Hash do arquivo b.txt é: {hash2.hexdigest()}')
else:
    print(f'O arquivo 1 "{arquivo1}"\né diferente do\narquivo 2 "{arquivo2}".')
