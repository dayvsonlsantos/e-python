"""

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""

# Meu código:

# palavra_secreta = 'perfume'
# palavra_revelada = '*******'

# letra_digitada = ''

# i = 0

# while len(letra_digitada) != 1:

#     while palavra_revelada != palavra_secreta:
#         letra_digitada = input('Digite uma letra: ')
        
#         if len(letra_digitada) == 1:
            
#             i = 0
            
#             for letra in palavra_secreta:
            
#                 if letra_digitada == palavra_secreta[i]:
#                     palavra_revelada[i] = palavra_secreta[i]
#                 else:
#                     palavra_revelada[i] += '*'
#                 i += 1
            
#         print(palavra_revelada)

# print('Você descobriu a palavra. Parabéns :)')

# Solução:

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
            
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print('Palavra Formada: ', palavra_formada)
            
    if palavra_secreta == palavra_formada:
        os.system('clear') 
        print('Você ganhou!! Parabéns!')
        print('Palavra Secreta: ', palavra_formada)
        print('Número de Tentativas: ',numero_tentativas)
        letras_acertadas = ''
        palavra_formada = ''
        numero_tentativas = 0