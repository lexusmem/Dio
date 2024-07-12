# first way to access
# from pymongo import MongoClient
# MONGODB_URI = 'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# client = MongoClient(MONGODB_URI)

# second way to access
import pprint
import pymongo as pyM

client = pyM.MongoClient(
    'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Dados do servidor do acesso
# print(client.server_info())

# criando db
# meu_db = client['simple_teste_db']
# criando colection
# minha_colection = meu_db['minha_colection_teste_db']
# Insira um documento para garantir que o banco de dados e a coleção sejam criados
# document = {"nome": "MongoDB", "tipo": "Banco de Dados NoSQL"}
# minha_colection.collection.insert_one(document)

# Listando os bancos de dados existentes na conexão
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(db_name)
print(10*'=')

# criando uma variavel que acessa o banco sample_airbnb
banco_airbnb = client['sample_airbnb']
# criando uma variavel que recebe as coleções do banco sample_airbnb
colecoes_airbnb = banco_airbnb.list_collection_names()
# Imprimindo todas as coleções existentes no banco de dados sample_airbnb
print(f'Coleções existente em {banco_airbnb.name}:')
for colecoes in colecoes_airbnb:
    print(colecoes)
print(10*'=')

# Listar todos os dados da coleção listingsAndReviews existe no banco de dados sample_airbnb

# Cria cariavel da coleção listingsAndReviews que existe dentro do banco sample_airbnb
colecao_sample_airbnb = banco_airbnb['listingsAndReviews']

# para impressão de todas os dados dentro da coleção listingsAndReviews
# for dados in colecao_sample_airbnb.find():
#     print(dados)

# para impressão do primeiro registro dentro da coleção listingsAndReviews
# print(colecao_sample_airbnb.find_one())

# formatado de forma melhor para visualização:
# pprint.pprint(colecao_sample_airbnb.find_one())

# formatado de forma melhor para visualização:
# pprint.pprint(colecao_sample_airbnb.find_one({"_id": "10038496"}))
