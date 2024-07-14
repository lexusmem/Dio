from sqlalchemy import create_engine

engine = create_engine("sqlite://")
print(engine)

conn = engine.connect()

# response = conn.execute('SELECT * FROM <NOME DA TABELA>;')

# for row in response:
#     print(row)
#     print('row.<nome_da_coluna>')
