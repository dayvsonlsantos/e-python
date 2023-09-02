"""

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
        Ou seja, quando mais distante da margem, ruim
    
"""

# No Python não temos constantes
# porém por convenção, utilizam as variáveis com
# letras toda em maiusculo, para simbolizar constantes

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

# \ -> indica quebra do código, para continuarmos embaixo

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
        print("Carro multado em radar 1")
        

# Esse código acima, podemos melhorá-lo atribuindo à variáveis:

velocidade_carro_no_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = velocidade_carro_no_radar_1 and carro_passou_radar_1
    
if carro_multado_radar_1:
        print("Carro multado em radar 1")