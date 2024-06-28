contatos = {
    'alex.sousa@gmail.com': {'nome': 'Alex', 'idade': 38, 'telefone': '11 96176-1340'}
}

remocao_1 = contatos.pop('nome', 'não encontrou a chave')
print(remocao_1)

print(contatos)
remocao_2 = contatos['alex.sousa@gmail.com'].pop('nome')
print(contatos)
contatos.pop('alex.sousa@gmail.com')
print(contatos)
