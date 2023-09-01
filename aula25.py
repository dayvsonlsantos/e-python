# Interporlação

# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF012342345)
    # x -> gera um hexadecimal minusculo
    # X -> gera um hexadecimal maiusculo

nome = 'Dayvson'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) # Interpolação
variavel2 = '{}, o preço é R${:.2f}'.format(nome, preco) # Format
variavel3 = f'{nome}, o preco é R${preco:.2f}' # f strings
print(variavel)
print(variavel2)
print(variavel3)


print('O Hexadecimal de %d é %08X' % (1500, 1500)) # esse 08 é para ele completar as casas com 0, para termos 8 digitos.