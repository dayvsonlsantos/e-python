# Calculadora

valor_informado_01 = input('Informe o 1º valor: ')

operacao_informada = input(
    'Informe a operaçao desejada: \n\n \
    + -> Soma \n \
    - -> Subtração \n \
    * -> Multiplicação \n \
    / -> Divisão \n\n \
Operação: '
)

valor_informado_02 = input('\nInforme o 2º valor: ')

operacao = 0

print('-'*20)

match operacao_informada:
    case "+":
        operacao = float(valor_informado_01) + float (valor_informado_02)
        print(f'\nA operação: {valor_informado_01} + {valor_informado_02} = {operacao:.2f}')
    case "-":
        operacao = float(valor_informado_01) - float (valor_informado_02)
        print(f'\nA operação: {valor_informado_01} - {valor_informado_02} = {operacao:.2f}')
    case "*":
        operacao = float(valor_informado_01) * float (valor_informado_02)
        print(f'\nA operação: {valor_informado_01} * {valor_informado_02} = {operacao:.2f}')
    case "/":
        if float(valor_informado_02) != 0:
            operacao = float(valor_informado_01) / float (valor_informado_02)
            print(f'\nA operação: {valor_informado_01} / {valor_informado_02} = {operacao:.2f}')
        else:
            print('\nNão é possível dividir por 0')
    case _:
        print('\nOperação desconhecida')