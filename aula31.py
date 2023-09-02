"""

Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade

"""

# P/ o python encontrar uma variável na memória,
# ele busca por sua identidade (id), p/ vermos:

v1 = 'a'
print(id(v1))

# P/ ser eficiente, o python verifica se os valores das
# variáveis são iguais. Caso for, essas possuirão o msm id

v2 = 'a'
print(id(v2))


condicao = False
passou_no_if = None # O indicado é sempre declararmos as variáveis fora do if

if condicao:
    print('faça algo')
else:
    print('Não faça algo')
    
print(passou_no_if, passou_no_if is None) # Geralmente usamos o is em vez do ==, com None