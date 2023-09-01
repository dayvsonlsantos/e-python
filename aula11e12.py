#... -> Ellipsis -> Não gera erros no código, é como um placeholder

#IMC = peso / (altura * altura)

nome = 'Dayvson Lima'
altura = 1.72
peso = 84
imc = ...

imc = peso / altura ** 2

print(nome, " tem ", altura, "de altura,\npesa ", peso, " quilos e seu IMC é \n", imc, sep='')
