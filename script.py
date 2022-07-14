import email


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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('-------------------')
    else:
        print('>>>>> Agenda vazia')


def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
    except KeyError:
        print('>>>>> Contato inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)

# requer 4 argumentos para editar/adicionar um contato


def incluir_editar_contato(contato):
    telefone = input('Digite o numero do telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f">>>>{contato} foi adicionado(a)/editado nos seus contatos.<<<<")


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print(f'>>>>>{contato} foi excluído(a) dos seus contatos')
    except KeyError:
        print('>>>>> Contato inexistênte')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)


def exportar_contato():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato};{telefone};{email};{endereco}\n')
        print('>>>>> Agenda exportada com sucesso')
    except:
        print('>>>>> Algum erro ocorreu ao exportar os contatos')


def imprimir_menu():
    print('---------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar arquivo CSV')
    print('0 - Fechar agenda')
    print('---------------------------------------')


while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>> Contato já existente:', contato)
        except KeyError:
            incluir_editar_contato(contato)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>> Editando contato: ', contato)
            incluir_editar_contato(contato)
        except KeyError:
            print('>>>>> Contato inexistente')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contato()
    elif opcao == '0':
        print('Fechando agenda')
        break
    else:
        print('Opção inválida')


incluir_editar_contato('maria', '990908989', 'maria@gmail.com', 'Rua ABC')
mostrar_contatos()
excluir_contato('matheus')
mostrar_contatos()
