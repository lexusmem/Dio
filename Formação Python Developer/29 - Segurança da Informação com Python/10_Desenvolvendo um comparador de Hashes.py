import hashlib
import os

# arquivo1 = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\29 - Segurança da Informação com Python\a.txt'
# arquivo2 = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\29 - Segurança da Informação com Python\b.txt'

caminho = r'C:\Users\lexus\Documents\Estudos_Programação\Dio\Formação Python Developer\29 - Segurança da Informação com Python'

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

caminho_arquivo1 = os.path.join(caminho, arquivo1)
caminho_arquivo2 = os.path.join(caminho, arquivo2)

hash1 = hashlib.new('ripemd160')
hash1.update(open(caminho_arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(caminho_arquivo2, 'rb').read())

if hash1.digest() == hash2.digest():
    print(f'O {arquivo1} é igual ao {arquivo2}.')
    print(f'Hash do arquivo {arquivo1} é: {hash1.hexdigest()}')
    print(f'Hash do arquivo {arquivo2} é: {hash2.hexdigest()}')
else:
    print(f'O arquivo 1: {arquivo1} é diferente do arquivo 2: {arquivo2}.')
    print(f'Hash do arquivo {arquivo1} é: {hash1.hexdigest()}')
    print(f'Hash do arquivo {arquivo2} é: {hash2.hexdigest()}')

'''
Caracteres (Modos) para Abertura de Arquivos em Python
Ao usar a função open() em Python para interagir com arquivos, você especifica um
"modo" que define a forma como o arquivo será acessado. Este modo é geralmente uma
string que combina um ou mais caracteres.

'r' - Abre para leitura (padrão). O arquivo deve existir. Se não existir,
um erro (FileNotFoundError) será gerado.

'w' - Abre para escrita. Se o arquivo existir, ele é truncado
(seu conteúdo é removido completamente) antes da escrita.
Se o arquivo não existir, ele é criado.

'x' - Abre para criação exclusiva. O arquivo é criado apenas se não existir.
Se o arquivo já existir, um erro (FileExistsError) será gerado.

'a' - Abre para escrita, anexando ao final do arquivo. Se o arquivo existir,
os novos dados são adicionados ao seu final. Se o arquivo não existir, ele é criado.

'b' - Modo binário. Usado em combinação com outros modos (ex: 'rb', 'wb', 'ab')
para indicar que o arquivo deve ser tratado como binário (bytes) e não como texto.

't' - Modo texto (padrão). Usado em combinação com outros modos (ex: 'rt', 'wt', 'at')
para indicar que o arquivo deve ser tratado como texto (strings).
É o padrão para 'r', 'w', 'x', 'a'.

'+' - Aberto para atualização (leitura e escrita). Usado em combinação com outros modos
(ex: 'r+', 'w+', 'a+', 'x+') para permitir tanto leitura quanto escrita no mesmo arquivo.
'''
