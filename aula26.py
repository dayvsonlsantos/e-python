'''
Formatação básica de Strings

s - string
d - int
f - float

.<número de dígitos>f
x ou X - Hexadecimal

(Caractere)(><^)(quantidade)

> - Preenche com caracteres a Esquerda
< - Preenche com caracteres a Direita
^ - Preenche com caracteres, para Centralizar

Sinal - + ou -
Ex.: 0>-100,.1f

Conversion flags - !r !s !a

'''

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel:0<10}.') # or print(f'{variavel:010}.')
print(f'{variavel: ^10}.')
print(f'{variavel:0^10}.') 
    # 0 -> É o caracte com o qual queremos preencher
    # ^ -> É a formatação
    # 10 -> Quant. de espaços p/ preencher
    
print(f'{1000.5348958934:+,.2f}')
    # , -> Coloca uma virgula, e reduz as casas decimais
    # + -> Exibe os números positivos com o sinal de + e negativos com o de -
    # - -> Exibe com sinal apenas os números negativos
    
print(f'{1000.5348958934:0>+10,.2f}')
    # Fazendo isso, com 0>+10 -> Conseguimos complentar com 0 os espaços ao redor, no caso, 10 espaços
    # Porém, assim o resultado será: 0+1,000.53
    # Para solucionar, fazemos:
print(f'{1000.5348958934:0=+10,.2f}')
    # = -> Força o número a aparecer antes dos zeros
    
print(f'O hexadecimal de 1500 é {1500:08x}')



