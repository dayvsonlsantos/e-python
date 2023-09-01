#Coletar dados do usuário

# Tudo que o usuário informa, quando armazenado, sempre será no tipo string
nome = input('Qual o seu nome? ')

idade = input('Qual a sua idade? ')

print(type(idade))

# Esse nome= -> Faz com que seja exibido: nome = valor_da_variavel
print(f'{nome=}')
print("O seu nome é {nomePessoa}".format(nomePessoa=nome))


# Forma iniciante de mudar o tipo da variável do input:

numero = int(input('Digite um número: '))
print(type(numero))
# De fato, resolve, no entanto, não é uma boa prática.
# Pois, quando o usuário digitar uma letra, quebrará o sistema.


# Outra forma, seria converter depois de uma chegagem:

outro_numero = input('Digite outro número: ')

# aqui faria a checagem, e depois:

# Como não fiz uma checagem ainda, dará o msm erro

int_numero = int(outro_numero);
print(type(int_numero))