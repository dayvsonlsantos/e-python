"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero_digitado = input('Informe um número inteiro: ')

    numeroPar = (int(numero_digitado)%2 == 0)

    if numeroPar:
        print(f'O número {numero_digitado} é um número par.')
    else:
        print(f'O número {numero_digitado} é um número ímpar')

except:
    print(f'Você digitou {numero_digitado}, isso não é um número inteiro')

    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


try:
    hora_informada = input('Informe a hora: ')

    int_hora_informada = int(hora_informada)

    bom_dia = (int_hora_informada >= 0 and int_hora_informada <= 11) or int_hora_informada == 24
    boa_tarde = int_hora_informada >= 12 and int_hora_informada <= 17
    boa_noite = int_hora_informada >= 18 and int_hora_informada <= 23

    if bom_dia:
        print('Bom dia')

    if boa_tarde:
        print('Boa tarde')
        
    if boa_noite:
        print('Boa noite')

except:
    print('Esse não é um horário válido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input('Informe o seu nome: ')

if nome_usuario.isdigit():
    print('Por favor, informe um nome, não número')
else:
    nome_curto = len(nome_usuario) <= 4
    nome_normal = len(nome_usuario) >= 5 and len(nome_usuario) <= 6
    nome_grande = len(nome_usuario) > 6

    if nome_curto:
        print(f'Seu nome, {nome_usuario}, é curto')
    elif nome_normal:
        print(f'Seu nome, {nome_usuario}, é normal')
    else:
        print(f'Seu nome, {nome_usuario}, é muito grande')