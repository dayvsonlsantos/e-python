"""

Introdução ao try/except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input(
    'Vou dobrar o número que você digitar: '
)

# isdigit() -> verifica se o valor possui apenas números.
# Caso seja decimal, terá ponto, portanto não será apenas
# numeros.

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

# Porém dessa forma, valores float cairá no else.

# O if não evita exceções (erros) de ocorrer
# Ele está apenas checando a lógica em códigos sem exceção

# Para solucionar de fato, podemos usar o try except
# Onde, quando ocorrer um erro, o programa automaticamente
# Pulará para o except.

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
    
# Obs.: Essa é uma forma mais simples p/ aprendizado