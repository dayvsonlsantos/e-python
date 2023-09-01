# Operadores lógicos

# and (e) or (ou) not (não)
# and -> todas as condições verdadeiras

# Também existe o tipo None que é
# usado para representar um não valor

# Valores avaliados como False são considerados Falsy.
# Valores avaliados como True são considerados Truthy.

'''

Valores Falsy

Sequências e coleções:
    Listas vazias []
    Tuplas vazias ()
    Dicionários vazios {}
    Sets vazios set()
    Strings vazias ""
    Ranges vazios range(0)
    Números

Zero de qualquer tipo numérico.
    Inteiro: 0
    De ponto flutuante: 0.0
    Complexo: 0j

Constantes
    None
    False


Valores Truthy:

Por padrão, um objeto é considerado verdadeiro.

Valores Truthy incluem:
    Sequências ou coleções não vazias (listas, tuplas, strings, dicionários, sets).
    Valores numéricos que não são zero.
    True

'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')
    


# Na verificação com And,

# Avaliação de curto circuito
    # O Python verifica as condições, se for True ele continua, caso seja Falsy, ele para ali.
    
print(True and False and True) #Imprime False -> Pois encontrou um Falsy (False)
print(True and 0 and True) #Imprime 0 -> Pois encontrou um Falsy (0 -> False)