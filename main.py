from lexico import recorrerCadena, construccionDeTabla
from sintactico import procesarSintaxis

entrada = ""
with open('entrada.txt', 'r') as file:
    entrada = file.read().replace('\n', '')

# LEXICO
simbolos, tipo_de_simbolo = recorrerCadena(entrada)
construccionDeTabla(simbolos, tipo_de_simbolo)

# SINTÁCTICO
procesarSintaxis(entrada=tipo_de_simbolo, simbolos=simbolos)

# SEMÁNTICO


