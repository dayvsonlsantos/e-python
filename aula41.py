# While/else

# Sempre que finalizar o while (sem erros ou break), executará o else

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado')