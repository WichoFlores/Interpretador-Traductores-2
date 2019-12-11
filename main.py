from lexico import recorrerCadena, construccionDeTabla
from sintactico import procesarSintaxis
from arbol import crearArbol
from semantico import validarSemantica

entrada = ""
with open('test.txt', 'r') as file:
    entrada = file.read().replace('\n', '')

# LEXICO
simbolos, tipo_de_simbolo = recorrerCadena(entrada)
construccionDeTabla(simbolos, tipo_de_simbolo)

# SINTÁCTICO
try:
    reglas_de_reduccion, simbolos_reducidos, valores_por_regla = procesarSintaxis(entrada=tipo_de_simbolo, simbolos=simbolos)
except:
    exit(0)

# ÁRBOL
crearArbol(reglas_de_reduccion[::-1], simbolos_reducidos[::-1], valores_por_regla[::-1])

# SEMÁNTICO
validarSemantica(valores_por_regla)