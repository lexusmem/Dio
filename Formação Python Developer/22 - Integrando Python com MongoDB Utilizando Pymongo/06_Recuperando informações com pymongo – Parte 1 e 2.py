import datetime
import pprint
import pymongo as pyM

client = pyM.MongoClient(
    'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Listando os bancos de dados existentes na conexão
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(db_name)
print(10*'=')

# Acessando banco simple_teste_db
banco_alex = client['sample_teste_db']
print(f'Coleções existente em {banco_alex.name}:')
# Variavel com as coleções do banco simple_teste_db
collection_banco_alex = banco_alex.list_collection_names()
# Imprimindo as coleções existentes no banco
for itens in collection_banco_alex:
    print(itens)
# Acessando dados que constam na coleção minha_colection_teste_db.collection
dados_colecao_alex = banco_alex['minha_colection_teste_db']
# Imprimindo o primeiro registro da coleção minha_colection_teste_db.collection
pprint.pprint(dados_colecao_alex.find_one())

# bulk inserts
# new_posts = [{
#     'author': 'camila',
#     'text': 'another post',
#     'tags': ['bulk', 'post', 'insert'],
#     'date': datetime.datetime.now()},
#     {
#     'author': 'sabrina',
#     'text': 'post from sabrina, new post available',
#     'title': 'Mongodb is fun',
#     'tags': ['bulk', 'post', 'insert'],
#     'date': datetime.datetime.now()}]

print(10*'=')
# print(f'Novo dados incluídos na coleção: {dados_colecao_alex.name}:')
# novos_dados = dados_colecao_alex.insert_many(new_posts)
# print(novos_dados.inserted_ids)
print('Todos os dados que consta na coleção: ')
for dados in dados_colecao_alex.find():
    pprint.pprint(dados)

print('Primeiro registro:')
pprint.pprint(dados_colecao_alex.find_one())

print('Buscando registro especifico:')
pprint.pprint(dados_colecao_alex.find_one({'author': 'sabrina'}))

print(f'Numero de registros na coleção {dados_colecao_alex.name}: {
      dados_colecao_alex.count_documents({})}')

print(f'Numero de registros com nome "alex" na {dados_colecao_alex.name}: {
      dados_colecao_alex.count_documents({'author': 'alex'})}')
