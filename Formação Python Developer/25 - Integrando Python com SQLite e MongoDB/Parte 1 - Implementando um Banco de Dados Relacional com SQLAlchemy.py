import datetime
from requests import delete
from sqlalchemy import create_engine, table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import inspect


# Configurações:
engine = create_engine("sqlite://")
Base = declarative_base()
session = Session(engine)
inspetor = inspect(engine)

print(engine)


# Entidades
class Cliente(Base):
    __tablename__ = "Cliente"
    # atibutos
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    cpf = Column(String(11))
    endereco = Column(String(50))

    conta = relationship('Conta', back_populates='cliente')

    # Representação das Classes
    def __repr__(self):
        return f"""
Id Cliente:\t{self.id}
Nome:\t\t{self.name}
CPF:\t\t{self.cpf}
Endereço:\t{self.endereco}
"""


# Entidades
class Conta(Base):
    __tablename__ = "Conta"
    # atibutos
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, default='Conta Corrente')
    agencia = Column(String)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'), nullable=False)
    saldo = Column(Float)
    data = datetime.date.today().strftime("%d/%m/%Y")

    cliente = relationship('Cliente', back_populates='conta')
    numero_conta = relationship('Numero', back_populates='conta_numero')

    # Representação das Classes
    def __repr__(self):
        return f"""
Id Conta:\t{self.id}
Tipo Conta:\t{self.tipo}
Agencia:\t{self.agencia}
Número Conta:\t{self.numero_conta}
Saldo:\t\t{self.saldo}
Data:\t\t{self.data}
"""


# Entidades
class Numero(Base):
    __tablename__ = "Numero"
    # atibutos
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_conta = Column(Integer, ForeignKey('Conta.id'), nullable=False)

    conta_numero = relationship('Conta', back_populates='numero_conta')

    def __repr__(self):
        return f'{self.id}'


print(Cliente.__tablename__)
print(Cliente.__table__)

print(Conta.__tablename__)
print(Conta.__table__)

print(Numero.__tablename__)
print(Numero.__table__)

# Criando esquema em nosso banco de dados SQLite de destino
# Usando nossos metadados de tabela e nosso mecanismo
Base.metadata.create_all(engine)

print('\nConsultando se as tabelas e o banco foram criadas.')

# Variavel com todas as tabelas do banco
tables = inspetor.get_table_names()

# variavel para cada tabela
table_one = tables[0]
table_two = tables[1]
table_three = tables[2]


print(f'Tabela - {table_one}')
print(inspetor.has_table(table_one))
print(f'Colunas da Tabela: {table_one}')
# variavel com as colunas da tabela
columns_one = inspetor.get_columns(table_one)
for columns in columns_one:
    print(columns)

print(f'\nTabela - {table_two}')
print(inspetor.has_table(table_two))
print(f'Colunas da Tabela: {table_two}')
# variavel com as colunas da tabela
columns_two = inspetor.get_columns(table_two)
for columns in columns_two:
    print(columns)
print('\n')

print(f'\nTabela - {table_three}')
print(inspetor.has_table(table_three))
print(f'Colunas da Tabela: {table_three}')
# variavel com as colunas da tabela
columns_three = inspetor.get_columns(table_three)
for columns in columns_three:
    print(columns)
print('\n')

# Sessões - Zona segura para transações
# SQL

# Insert - inserindo dados nas tabelas
# Instanciando as classes e criando variáveis com dados para inserir os dados no banco
conta_alex = Cliente(
    name='Alex Silva de Sousa',
    cpf='22920975838',
    endereco='Rua Antonio Fernandes, 137',
    conta=[Conta(agencia='0001', saldo=21500.00, numero_conta=[Numero()])]
)

conta_pamela = Cliente(
    name='Pamela de Melo Rodrigues',
    cpf='30221808027',
    endereco='Rua Silas, 246',
    conta=[Conta(agencia='0001', saldo=47857.25, numero_conta=[Numero()])]
)

# Consistindo dados no banco - inserindo dados no banco
# session.add(conta_alex)
session.add_all([conta_alex, conta_pamela])
session.commit()

# select
print('Dadas das tabelas - Primeira Impressão')
print(table_one)
# Recuperar dados do banco
data_cliente = session.query(Cliente).all()
print(data_cliente)
print(10*'=')
print(table_two)
# Recuperar dados do banco
data_conta = session.query(Conta).all()
print(data_conta)

# delete
session.query(Cliente).filter(Cliente.name == 'Alex Silva de Sousa').delete()
session.commit()

# alteração - update
session.query(Cliente).filter(Cliente.name == 'Pamela de Melo Rodrigues').update(
    {'endereco': 'Rua Silas, 5000'})
session.commit()

# select
print('Dadas das tabelas - Segunda Impressão')
print(table_one)
# Recuperar dados do banco
data_cliente = session.query(Cliente).all()
print(data_cliente)
print(10*'=')
print(table_two)
# Recuperar dados do banco
data_conta = session.query(Conta).all()
print(data_conta)


# Acessando dados individuais
print(10*'=')
print(data_cliente[0])
print(10*'=')
print(data_cliente[0].name)

# Fechando a conexão
session.close()
