# Comentário no Python -> O Interpretador Python ignora;

"""
DocString
    Não é um comentário, o Interpretador ler, mas não executa os códigos dentro.
    É usado para documentação
"""

'''
    Também é uma DocString
'''

# sep -> Separador, defino o separador. Por padrão, já vem o Space;
print(12,34) # Resultado: 12 34
print(12,34, sep='') # Resultado: 1234
# end -> Altera o final do print
print(12,34, end='##') # Resultado: 12 34##. Por padrão, já vem o \n (quebra de linha)

# Quebras de Linhas:

# \r\n -> CRLF
# \n -> LF