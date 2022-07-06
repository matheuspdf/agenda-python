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


# requer 4 argumentos para editar/adicionar um contato
def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f">>>>{contato} foi adicionado(a)/editado nos seus contatos.<<<<")


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f'{contato} foi excluído(a) dos seus contatos')


incluir_editar_contato('maria', '990908989', 'maria@gmail.com', 'Rua ABC')
mostrar_contatos()
excluir_contato('matheus')
mostrar_contatos()
