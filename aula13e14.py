#Formatação -> f-strings

nome = 'Dayvson Lima'
altura = 1.72
peso = 84
imc = ...

imc = peso / altura ** 2

# O f indica o f-strings
# altura:.2f -> Significa 2 casas decimais
resultado = f'{nome} tem {altura:.2f} de altura,\npesa {peso} quilos e seu IMC é\n{imc:.2f}'

print(nome, " tem ", altura, " de altura,\npesa ", peso, " quilos e seu IMC é \n", imc, sep='')
print('\n')
print(resultado)

print('\n')


#Formatação -> format -> método (ação de um objeto) no python

a = 'A'
b = 'B'
c = 1.1

# cada chave, se referência ao respectivo valor no format, seguindo a ordem.

# string = 'a={} b={} c={:.2f}'

#formato = string.format(a, b, c) #a, b, c -> São parâmetros



# Mas, podemos passar os indices também:

# string = 'a={0} a={0} b={1} c={2:.2f}' #:.2f -> Determinando p/ exibir duas casas decimais

# formato = string.format(a, b, c) #a, b, c -> São parâmetros



# Além disso, podemos nomear os indices (parâmetros nomeados), tornando-os mais confiáveis
string = 'a={nome1} b={nome2} c={nome3:.2f}'

# Ao usar parâmetros nomeados, tudo que vem depois dele, também precisa ser nomeado
formato = string.format(nome1=a, nome2=b, nome3=c) #a, b, c -> São parâmetros

print(formato)




print('\n{} tem {:.2f} de altura,\npesa {} quilos e seu IMC é de\n{:.2f}'.format(nome, altura, peso, imc))


