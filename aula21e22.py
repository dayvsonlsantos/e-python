# Or -> Qualquer condição verdadeira, torna a expresão toda verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# Para evitar que a lógica (OR e AND) fica ambigua, colocamos entre parenteses
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
# Avaliação de curto circuito
# -> Fizemos uma verificação de senha (se foi preenchida), sem usar o if
senha = input('Senha: ') or 'Sem senha'
print(senha)