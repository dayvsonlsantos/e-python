# Not

# Usado p/ inverter expressões
# not True = False
# not False = True

senha = 1

# Invertemos o valor True (pois senha = 1, então é Truthy), para Falsy
if not senha:
    print('Você não digitou nada')