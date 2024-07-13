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

# Deletando um Banco de Dados
# client.drop_database['sample_teste_db']
