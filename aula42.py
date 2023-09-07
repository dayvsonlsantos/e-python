# Qual letra apareceu mais ?

frase = 'O Python é uma linguagem de programação' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'.lower()
    
# Existe o metodo count -> Realiza a contagem de algo

i = 0

qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_mais_apareceu = letra_atual
    
    print(f'{letra_atual} = {quantas_vezes_letra_apareceu}')
    i += 1
    
print(f'\n\n{letra_que_mais_apareceu} = {qtd_apareceu_mais_vezes}')