# first way to access
# digitar senha correta quando for utilizar o acesso ao banco
import pprint
from pymongo import MongoClient
import datetime

from requests import delete

MONGODB_URI = 'mongodb+srv://lexusmem:12345@cluster0.gdsqwuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(MONGODB_URI)

# Dados do servidor do acesso
print(client.server_info())

# criando db
meu_db = client['desafio_dio']
# criando collection
minha_colection = meu_db['collection_bank']

#  Insira um documento para garantir que o banco de dados e a coleção sejam criados
document_1 = {
    'id_cliente': 1,
    'nome': 'Alex Silva de Sousa',
    'cpf': 22920975838,
    'endereco': 'Rua Antonio Fernandas, 137',
    'tipo_conta': 'Conta Corrente',
    'agencia': '0001',
    'num_conta': 1,
    'date': datetime.date.today().strftime("%d/%m/%Y")}

document_2 = {
    'id_cliente': 2,
    'nome': 'Pamela de Melo Rodrigues',
    'cpf': 30221808027,
    'endereco': 'Rua Silas, 249',
    'tipo_conta': 'Conta Corrente',
    'agencia': '0001',
    'num_conta': 2,
    'date': datetime.date.today().strftime("%d/%m/%Y")}

document_3 = {
    'id_cliente': 3,
    'nome': 'Item para Exclusão',
    'cpf': 30221809037,
    'endereco': 'Rua Silas, 1000',
    'tipo_conta': 'Conta Corrente',
    'agencia': '0001',
    'num_conta': 3,
    'date': datetime.date.today().strftime("%d/%m/%Y")}

# Inserindo na collection criada no BD
minha_colection.insert_many([document_1, document_2, document_3])

# Listando os bancos de dados existentes na conexão
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(db_name)
print(f"\n{10*'='}\n")

print('Collections existente no Banco de Dados:')
# variavel para acessar o banco criado
banco_dio = client['desafio_dio']
# recuperando collections do banco
print(banco_dio.list_collection_names())
print(f"\n{10*'='}\n")

print('Dados existentes dentro da Collection')
# variavel da collection criada
collection_bank = banco_dio['collection_bank']
# dados da collectio
print
for collection in collection_bank.find():
    pprint.pprint(collection)
print(f"\n{10*'='}\n")

# alteração de valor
print("Update do dados de endereço")
collection_bank.update_one(
    {'id_cliente': 2}, {'$set': {'endereco': 'Rua Silas, 246'}})
pprint.pprint(collection_bank.find_one({"id_cliente": 2}))
print(f"\n{10*'='}\n")

# exclusão dos dados collection
print('Deletando 1 registro da coleção')
collection_bank.delete_one({'id_cliente': 3})
for collection in collection_bank.find():
    pprint.pprint(collection)
print(f"\n{10*'='}\n")

# exclusão de todos os collection
print('Deletando todos os registros da coleção')
collection_bank.delete_many({})
for collection in collection_bank.find():
    pprint.pprint(collection)
print(banco_dio.list_collection_names())
print(f"\n{10*'='}\n")

# exclusão da collection
print('Deletando a Collection')
banco_dio['collection_bank'].drop()
print(f"\n{10*'='}\n")

# exclusão do BD
print('Deletando o Banco de Dados')
client.drop_database(banco_dio)
print('Lista de Bancos de Dados existentes na conexão:')
print(client.__str__)
for db_name in client.list_database_names():
    print(db_name)
print(f"\n{10*'='}\n")
