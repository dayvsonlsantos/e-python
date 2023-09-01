# Operadores in (está entre) e not in (não está entre)
# String são iteráveis
#   iteráveis -> significa que podemos navegar item por item,
#   utilizando os índices, tanto positivo quanto negativo.

# Exemplos:
# 0 1 2 3 4 5 6
# D a y v s o n
#-7-6-5-4-3-2-1

nome = 'Dayvson'
print(nome[2])
print(nome[-5])

print('a' in nome) # verifica se a letra 'a' está na variável nome
print('ayv' in nome) # verifica se as letras 'ayv' estão na variável nome

print(10 * '-')

print('vio' not in nome) # verifica se as letras 'vio' NÃO estão na variável nome

# Lembre-se: Strings em Python são iteráveis!

'''

Qual o resultado do código abaixo?

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)

Resp: 1 1 -> Pois o OR busca a primeira verdade na expresão. Nesses caso
            o valor verdadeiro é o 1, pois é um Truthy e o 0 um Falsy.

'''

nome = input('Digite o seu nome: ')
deseja_encontrar = input('Digite o que deseja encontrar no seu nome: ')

if deseja_encontrar in nome:
    print(f'{deseja_encontrar} está em {nome}')
else:
    print('{} não está em {}'.format(deseja_encontrar, nome))