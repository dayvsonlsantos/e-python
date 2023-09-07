# Como funciona o for no Python?

'''

Iterável -> É um elemento que tem um método dentro dele
chamado de __iter__
    # para chama-lo usamosL iter('texto') ou texto.__iter__()
    Iter -> Me entrega seu iterador

Iterador -> Quem sabe entregar um valor por vez

Possuindo o Iterador, podemos chamar a função next.

Next -> me entrega o próximo valor

print(texto.__next__())

'''

# texto = iter('Dayvson')

# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto)) # -> Retorna StopIteration

# Ao final dos elementos, será retornado um erro, chamado: StopIteration
# Isso avisa ao for para encerrar a repetição.

# Como funciona o for:

texto = 'Dayvson'
iterator = iter(texto)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break