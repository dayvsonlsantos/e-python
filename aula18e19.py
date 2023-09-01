# Operadores de comparação (relacionais)

'''

> -> Maior que
>= -> Maior ou igual
< -> Menor
<= -> Menor ou igual
== -> Igual
!= -> Diferente

'''

primeiro_valor = input ('Digite um valor: ')
segundo_valor = input ('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior'
        f'do que {segundo_valor=}'
    )
elif segundo_valor > primeiro_valor:
    print('segundo_valor={} é maior do que primeiro_valor={}'.format(segundo_valor, primeiro_valor))
else:
    print('Os valores são iguais')