# Iterando strings com while

nome = 'Dayvson Lima'
novo_nome = ''
contador = 0

print(f'Nome: {nome}')

while contador < len(nome):
    novo_nome += f'*{nome[contador]}'
    contador += 1

print(f'Novo nome: {novo_nome}')