import pprint
import pymongo as pyM

client = pyM.MongoClient(
    'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Listando os bancos de dados existentes na conexão
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(db_name)
print('')
print(10*'=')

print('Collections de DB Alex:')
db_alex = client['sample_teste_db']
print(db_alex.list_collection_names())

print('')
print(10*'=')
print('Acessando os dados da Collections de DB Alex:')
collection_db_alex = db_alex['minha_colection_teste_db']
pprint.pprint(collection_db_alex.find_one())


print('')
print(10*'=')
print('Acessando os dados da Collections de DB Alex ordenada:')
for dados in collection_db_alex.find().sort('_id'):
    pprint.pprint(dados)

print('')
print(10*'=')

# criação de índice
indices = db_alex.profiles.create_index(
    [('author', pyM.ASCENDING)], unique=True)
print('Índice criado: ')
print(sorted(list(db_alex.profiles.index_information())))

user_profile = [
    {'user_id': 211, 'name': 'alex'},
    {'user_id': 212, 'name': 'joao'},
]

# criando coleção profile_user e inserindo user_profile:
result = db_alex.profile_user.insert_many(user_profile)

print(db_alex.list_collection_names())

collections = db_alex.list_collection_names()
for collection in collections:
    print(collection)
