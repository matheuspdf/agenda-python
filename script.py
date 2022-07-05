AGENDA = {}


AGENDA['matheus'] = {
    'telefone': '956872345',
    'email': 'matheus@mail.com',
    'endereco': 'Rua 1',
}
AGENDA['joão'] = {
    'telefone': '989567845',
    'email': 'joao@mail.com',
    'endereco': 'Rua 2',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('-------------------')


def buscar_contato(contato):
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]['telefone'])
    print("Email:", AGENDA[contato]['email'])
    print("Endereço:", AGENDA[contato]['endereco'])


mostrar_contatos()
buscar_contato('joão')
