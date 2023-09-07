# For + range
# range -> range (start, stop, step)

# esse Range é independente do for,
# inclusive, range é uma variável reservada no python;

numeros = range(10) #Podemos passar: start, stop e step.
# Caso passemos apenas um valor, esse será o stop.
# E assim, o start será 0, e o step virá 1.
# Lembrando que no python, o último valor
# não é incluído

print(numeros)

for numero in numeros:
    print(numero)

numeros = range(5,10)

print(numeros)

for numero in numeros:
    print(numero)

numeros = range(5,10,2)

print(numeros)

# Lembrando: com For não nos preocupamos com indices,
# nele nós pegamos o valor:

for numero in numeros:
    print(numero)
    

numeros = range(0,-10, -2)

print(numeros)

for numero in numeros:
    print(numero)
