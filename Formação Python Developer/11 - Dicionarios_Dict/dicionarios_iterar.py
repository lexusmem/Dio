contatos = {
    'alex.sousa@gmail.com': {'nome': 'Alex', 'idade': 38, 'telefone': '11 96176-1340'},
    'laura@gmail.com': {'nome': 'laura', 'idade': 8, 'telefone': '11 91010-1010'},
    'pamela@gmail.com': {'nome': 'pamela', 'idade': 35, 'telefone': '11 91111-1111'},

}
for chave in contatos:
    print(chave, contatos[chave])
print(70 * "=")
print(contatos['alex.sousa@gmail.com'])
print(70 * "=")
for chave, valor in contatos.items():
    print(chave, valor)
