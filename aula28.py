'''

Exercício

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}

Se nada for digitado em nome e idade:
    exiba "Desculpe, você deixou campos vazios"

'''

nomeDoUsuario = input('Informe o seu nome: ')
idadeDoUsuario = input('Informe a sua idade: ')

if nomeDoUsuario and idadeDoUsuario:
    print(f'Seu nome é {nomeDoUsuario}')
    print('Seu nome invertido é {}'.format(nomeDoUsuario[-1:-len(nomeDoUsuario)-1:-1]))
    print('Seu nome invertido é {}'.format(nomeDoUsuario[::-1]))
    if ' ' in nomeDoUsuario:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nomeDoUsuario)} letras')
    print('A primeira letra do seu nome é %s' % (nomeDoUsuario[0]))
    print(f'A última letra do seu nome é {nomeDoUsuario[-1]:}')
else:
    print('Desculpe, você deixou campos vazios')