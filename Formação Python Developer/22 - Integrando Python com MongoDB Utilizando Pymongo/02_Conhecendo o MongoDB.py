# MongDB
"""
O banco de dados NoSQL de alta performance que conquista o mundo do
desenvolvimento.

* BD NoSql
* Orientado a documentos
* Flexível
* Schema opcional
"""

"""
O que são coleções no MongDB

Coleções (ou "collections" em inglês) são conjuntos de documentos.
Elas são semelhantes a tabelas em um banco de dados relacional.
As coleções são como os conjuntos flexíveis de documentos.

Estrutura Flexível: Ao contrário das tabelas em bancos de dados relacionais, as coleções no MongoDB não têm um esquema fixo.
Documentos: Em vez de linhas, como em uma tabela relacional, as coleções contêm documentos. Cada documento é um objeto BSON (Binary JSON) que pode conter dados complexos, incluindo arrays e documentos aninhados.
Sem Tipagem Fixa: Não é necessário definir tipos de dados para os campos em uma coleção. Você pode inserir qualquer tipo de dado em qualquer campo, e documentos diferentes na mesma coleção podem ter campos diferentes.
Índices: Assim como em bancos de dados relacionais, você pode criar índices em campos dentro de documentos de uma coleção para melhorar o desempenho das consultas.
Operações de Banco de Dados: As coleções suportam uma variedade de operações de banco de dados, como inserção, atualização, deleção e consultas.
"""

"""
Exemplo de Documentos em uma Coleção:
Aqui está um exemplo de dois documentos em uma coleção chamada "usuarios":

{
   "_id": 1,
   "nome": "João",
   "idade": 30,
   "email": "joao@example.com"
}

{
   "_id": 2,
   "nome": "Maria",
   "idade": 25,
   "email": "maria@example.com",
   "endereco": {
      "rua": "Rua das Flores",
      "cidade": "São Paulo"
   }
}
"""

"""
Namespace
No contexto do MongoDB, um namespace é uma combinação do nome do banco de dados
e do nome da coleção, separados por um ponto. Por exemplo, se você tem um
banco de dados chamado "meuBanco" e uma coleção chamada "minhaColecao",
o namespace completo para essa coleção seria "meuBanco.minhaColecao".

Exemplo de Namespaces
Vamos supor que você tenha as seguintes coleções em diferentes bancos de dados:

Banco de Dados: escola
Coleção: alunos
Namespace: escola.alunos
================
Banco de Dados: empresa
Coleção: funcionarios
Namespace: empresa.funcionarios
"""
