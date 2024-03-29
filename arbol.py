from prettytable import PrettyTable

definicion_de_reglas = {
  1: ["Definiciones"],
  2: [],
  3: ["Definicion", "Definiciones"],
  4: ["DefVar"],
  5: ["DefFunc"],
  6: ["tipo", "identificador" , "ListaVar", "punto y coma"],
  7: [],
  8: ["identificador", "ListaVar"],
  9: ["tipo", "identificador", "parentesis apertura", "Parametros", "parentesis cierre", "BloqFunc"],
  10: [],
  11: ["tipo", "identificador", "ListaParam"],
  12: [],
  13: ["coma", "tipo", "identificador", "ListaParam"],
  14: ["llave apertura", "DefLocales", "llave cierre"],
  15: [],
  16: ["DefLocal", "DefLocales"],
  17: ["DefVar"],
  18: ["Sentencia"],
  19: [],
  20: ["Sentencia", "Sentencias"],
  21: ["identificador", "igual", "Expresion", "punto y coma"],
  22: ["if", "parentesis apertura", "Expresion", "parentesis cierre", "SentenciaBloque", "Otro"],
  23: ["while", "parentesis apertura", "Expresion", "parentesis cierre", "Bloque"],
  24: ["return", "ValorRegresa", "punto y coma"],
  25: ["LlamadaFunc"],
  26: [],
  27: ["else", "SentenciaBloque"],
  28: ["llave apertura", "Sentencias", "llave cierre"],
  29: [],
  30: ["Expresion"],
  31: [],
  32: ["Expresion", "ListaArgumentos"],
  33: [],
  34: ["coma", "Expresion", "ListaArgumentos"],
  35: ["llave aperturalamadaFunc"],
  36: ["identificador"],
  37: ["entero"],
  38: ["real"],
  39: ["cadena"],
  40: ["identificador", "parentesis apertura", "Argumentos", "parentesis cierre"],
  41: ["Sentencia"],
  42: ["Bloque"],
  43: ["parentesis apertura", "Expresion", "parentesis cierre"],
  44: ["opSuma", "Expresion"],
  45: ["opNot", "Expresion"],
  46: ["Expresion", "opMul", "Expresion"],
  47: ["Expresion", "opSuma", "Expresion"],
  48: ["Expresion", "opRelac", "Expresion"],
  49: ["Expresion", "opIgualdad", "Expresion"],
  50: ["Expresion", "opAnd", "Expresion"],
  51: ["Expresion", "opOr", "Expresion"],
  52: ["Termino"],
}

def crearArbol(reglas_de_reduccion, simbolos_reducidos, valores_por_regla):
  t = PrettyTable()
  t.field_names = ["REGLA", "VALORES"]

  for simbolos, regla, valor in zip(simbolos_reducidos, reglas_de_reduccion, valores_por_regla):
    t.add_row([regla, valor])
    # print("Regla: {} -> {}".format(regla, definicion_de_reglas[regla]))
    # print("Simbolos Obtenidos: ", simbolos)
    # if (simbolos == definicion_de_reglas[regla]):
    #   print("Válido.")
    # else:
    #   print("Inválido.")
  print(t)