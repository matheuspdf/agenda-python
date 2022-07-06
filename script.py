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


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')


imprimir_menu()

opcao = input('Escolha uma opção: ')
if opcao == '1':
    mostrar_contatos()
elif opcao == '2':
    contato = input('Digite o nome do contato: ')
    buscar_contato(contato)
elif opcao == '3' or opcao == '4':
    contato = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço: ')
    incluir_editar_contato(contato, telefone, email, endereco)
elif opcao == '5':
    contato = input('Digite o nome do contato: ')
    excluir_contato(contato)
elif opcao == '0':
    print('Fechando agenda')
else:
    print('Opção inválida')


incluir_editar_contato('maria', '990908989', 'maria@gmail.com', 'Rua ABC')
mostrar_contatos()
excluir_contato('matheus')
mostrar_contatos()
