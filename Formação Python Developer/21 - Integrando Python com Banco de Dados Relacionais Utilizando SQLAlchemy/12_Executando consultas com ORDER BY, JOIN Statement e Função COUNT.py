import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import func

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # atibutos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname}'


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f'Address(id={self.id}, email_address={self.email_address})'


print(User.__tablename__)
print(User.__table__)

print(Address.__tablename__)
print(Address.__table__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.has_table("address"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.get_columns("address"))
print(inspetor_engine.get_columns("user_account"))

# nome do banco de dados
print(inspetor_engine.default_schema_name)

# Inserindo dados nas tabelas
with Session(engine) as session:
        alex = User(
            name='alex',
            fullname='alex silva de sousa',
            address=[Address(email_address='lexusmem@gmail.com')]
        )

        laura = User(
            name='laura',
            fullname='laura de melo rodrigues',
            address=[Address(email_address='laura@gmail.com'),
                     Address(email_address='laura2@gmail.com')]
        )

        pamela = User(name='pamela', fullname='pamela de melo rodrigues')

        # enviando para o BD(persistência de dados)
        session.add_all([alex, laura, pamela])

        # commitando tuplas digitadas no banco10_Criando uma Sessão para Persistir dados no SQlite.py
        session.commit()

stmt = select(User).where(User.name.in_(['alex', 'pamela', 'laura']))
print('\nRecuperando usuarios apartir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando endereços de e-mail's apartir de condição de filtragem")
for address in session.scalars(stmt_address):
    print(address)

print("\nSelect executado para busca usuarios de maneira ordenada por nome")
print(select(User).order_by(User.fullname.desc()))
print("===Recuperando Informações de maneira ordenada Usuarios===")
stmt_order_user = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order_user):
    print(result)

print("\nSelect executado para busca e-mail's de maneira ordenada por id")
print(select(Address).order_by(Address.id.asc()))
print("===Recuperando Informações de maneira ordenada E-mail===")
stmt_order_address = select(Address).order_by(Address.id.asc())
for result in session.scalars(stmt_order_address):
    print(result)

print("\nSelect executado para busca realizar join entre usuario e email's")
print(select(User.fullname, Address.email_address).join_from(Address, User))
print("===Recuperando Informações de Usuarios e E-mail===")
stmt_join_user_address = select(User.fullname, Address.email_address).join_from(Address, User)
connection = engine.connect()
results = connection.execute(stmt_join_user_address).fetchall()
for result in results:
    print(result)

print("\nContando o numero de instancias que consta na tabela Usuarios")
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)

print("\nContando o numero de instancias que consta na tabela Email")
stmt_count = select(func.count('*')).select_from(Address)
for result in session.scalars(stmt_count):
    print(result)
