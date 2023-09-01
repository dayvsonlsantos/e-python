'''

Fatiamento de Strings
 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]

Obs.: a função len retorna a qtd
de carateres da str

'''

# Lembrando: As Strings no Python são iteráveis

variavel = 'Olá Mundo'

# Definindo o indice inicial e final + 1 que quero pegar
    # No python, ele geralmente omite o indice final, assim, pegamos 1 na frente
print(variavel[4:8]) # Result: Mund
print(variavel[4:]) # Result: Mundo -> Omitindo o final, ele irá até o final
print(variavel[:3]) # Result: Olá -> Omitindo o inicio, ele começará no 0

print(len(variavel)) #Retorna a quant. de caracteres -> 9

print(variavel[0:len(variavel):1])
    #[inicio, final (total de caracteres), passo (de quanto ele irá pular)]
    
# Também podemos usar o passo invertido, o que irá inverter a String
# Porém para isso, temos que usar o fatiamento no negativo:

print(variavel[-1:-len(variavel)-1:-1]) # Result: odnuM álO
    # Esse -len(variavel) -> Equivale a -9. Porém como o python omite o último
    # Coloco -len(variavel)-1, que será -9-1, logo -10