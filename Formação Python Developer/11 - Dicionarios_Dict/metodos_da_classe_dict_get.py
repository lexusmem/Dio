contatos = {
    'alex.sousa@gmail.com': {'nome': 'Alex', 'idade': 38, 'telefone': '11 96176-1340'}
}

# contatos['chave']
print(contatos.get('chave'))
resultado = contatos.get('chave', {})
print(resultado)
print(contatos.get('alex.sousa@gmail.com', {}))
