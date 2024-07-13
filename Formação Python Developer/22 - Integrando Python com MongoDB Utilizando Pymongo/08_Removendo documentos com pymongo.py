import pprint
import pymongo as pyM

client = pyM.MongoClient(
    'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Listando os bancos de dados existentes na conexão
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(f"* {db_name}")
print('')
print(10*'=')

print('Collections de DB Alex:')
db_alex = client['sample_teste_db']

# # removendo AS COLEÇÕES:
# db_alex['profiles'].drop()
# db_alex['profile_user'].drop()

# # removendo os dados as coleções
# db_alex.minha_colection_teste_db.drop()


for collection in db_alex.list_collection_names():
    print(f'Nome da Coleção: {collection}')
    print('dados da coleção:')
    colecao = db_alex[collection]
    for dados in colecao.find():
        pprint.pprint(dados)
print('')
print(10*'=')

# deletar apenas um dos registros
colecao = db_alex['minha_colection_teste_db']
print(colecao.delete_one({'author': 'alex'}))
print('')
print(10*'=')

for dados in colecao.find():
    pprint.pprint(dados)
