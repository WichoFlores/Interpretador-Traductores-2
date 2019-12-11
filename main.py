from lexico import recorrerCadena, construccionDeTabla
from sintactico import procesarSintaxis
from semantico import procesarSemantica

entrada = ""
with open('entrada.txt', 'r') as file:
    entrada = file.read().replace('\n', '')

# LEXICO
simbolos, tipo_de_simbolo = recorrerCadena(entrada)
construccionDeTabla(simbolos, tipo_de_simbolo)

# SINTÁCTICO
reglas_de_reduccion, simbolos_reducidos, valores = procesarSintaxis(entrada=tipo_de_simbolo, simbolos=simbolos)
print(valores)
# SEMÁNTICO
procesarSemantica(reglas_de_reduccion[::-1], simbolos_reducidos[::-1])

