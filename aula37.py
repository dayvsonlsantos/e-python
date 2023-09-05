contador = 0

while contador < 10:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6')
        continue #Faz com que pule o que vem depois, e continue o loop
    
    print(contador)
    
print('Acabou')