import re
from prettytable import PrettyTable

# Léxico
tabla_de_simbolos = {
  0: "identificador",
  1: "entero",
  2: "real",
  3: "cadena",
  4: "tipo",
  5: "opSuma",
  6: "opMul",
  7: "opRelac",
  8: "opOr",
  9: "opAnd",
  10: "opNot",
  11: "opigualdad",
  12: "punto y coma",
  13: "coma",
  14: "parentesis apertura",
  15: "parentesis cierre",
  16: "llave apertura",
  17: "llave cierre",
  18: "igual",
  19: "if",
  20: "while",
  21: "return",
  22: "else",
  23: "$",
  24: "programa",
  25: "Definiciones",
  26: "Definicion",
  27: "DefVar",
  28: "ListaVar",
  29: "DefFunc",
  30: "Parametros",
  31: "ListaParam",
  32: "BloqFunc",
  33: "DefLocales",
  34: "DefLocal",
  35: "Sentencias",
  36: "Sentencia",
  37: "Otro",
  38: "Bloque",
  39: "ValorRegresa",
  40: "Argumentos",
  41: "ListaArgumentos",
  42: "Termino",
  43: "LlamadaFunc",
  44: "SentenciaBloque",
  45: "Expresion"
}

simbolos_lexicos = {
  "identificador": 0,
  "entero": 1,
  "real": 2,
  "cadena": 3,
  "int": 4,
  "float": 4,
  "void": 4,
  "+": 5,
  "-": 5,
  "*": 6,
  "/": 6,
  "<": 7,
  "<=": 7,
  ">": 7,
  ">=": 7,
  "||": 8,
  "&&": 9,
  "!": 10,
  "!=": 11,
  "==": 11,
  ";": 12,
  ",": 13,
  "(": 14,
  ")": 15,
  "{": 16,
  "}": 17,
  "=": 18,
  "if": 19,
  "while": 20,
  "return": 21,
  "else": 22,
  "$": 23,
}

def recorrerCadena(cadena):
  simbolos = []
  tipo_de_simbolo = []

  while cadena:
    print(cadena)
    isReal = False
    matched = False
    
    # Validar si es alfanumérico
    substring = ""
    for caracter in cadena:
      substring += caracter
      # Si encuentra espacio y quitándoselo no entra en el regex, entonces saltar
      if caracter == " " and not re.search("^[A-Za-z][A-Za-z0-9_-]*$", substring[0:-1]):
        break
      if not re.search("^[A-Za-z][A-Za-z0-9_-]*$", substring) or len(substring) == len(cadena):
        matched = True
        if not len(substring) == len(cadena) or not re.search("^[A-Za-z][A-Za-z0-9_-]*$", substring):
          substring = substring[0:-1]

        if re.search("^[A-Za-z][A-Za-z0-9_-]*$", substring): 
          cadena = cadena[len(substring):].strip()

          if substring in ["int", "float", "void"]:
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos[substring])
          elif substring == "if":
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos[substring])
          elif substring == "while":
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos[substring])
          elif substring == "return":
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos[substring])
          elif substring == "else":
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos[substring])
          else:
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos["identificador"])
          break

    if matched == True:
      matched = False
      pass
    
    # Validar si es entero
    substring = ""
    if not isReal:
      for caracter in cadena:
        substring += caracter
        if caracter == " " and not re.search("^[0-9]+$", substring[0:-1]):
          break
        if not re.search("^[0-9]+$", substring) or len(substring) == len(cadena):
          # If it's because of a decimal point, it's a float
          if caracter == ".":
            isReal = True
            break

          if not len(substring) == len(cadena) or not re.search("^[0-9]+$", substring):
            substring = substring[0:-1]
          
          if re.search("^[0-9]+$", substring):
            simbolos.append(substring)
            tipo_de_simbolo.append(simbolos_lexicos["entero"])
            matched = True
            break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

    # Validar si es real
    substring = ""
    for caracter in cadena:
      substring += caracter
      if caracter == " " and not re.search("^[+-]?[0-9]+\.[0-9]+$", substring[0:-1]):
        break
      if re.search("[+-]?[0-9]+\.[0-9]+", substring[0:-1]) and re.search("[^0-9]", caracter):
        substring = substring[0:-1]
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos["real"])
        isReal = False
        matched = True
        break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

    # Validar si es igual o igualdad
    substring = ""
    for caracter in cadena:
      substring += caracter
      if not substring == "=":
        if substring[0] != "=":
          break
        if substring == "==":
          simbolos.append(substring)
          tipo_de_simbolo.append(simbolos_lexicos[substring])
          matched = True
          break
        else:
          substring = substring[0:-1]
          simbolos.append(substring)
          tipo_de_simbolo.append(simbolos_lexicos[substring])
          matched = True
          break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

    # Validar si es punto y coma
    substring=""
    for caracter in cadena:
      substring += caracter
      if substring == ";":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

    # Validar si es opSuma
    substring=""
    for caracter in cadena:
      substring += caracter
      if substring == "+":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break
      elif substring == "-":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass
    
    # Validar si es paréntesis
    substring=""
    for caracter in cadena:
      substring += caracter
      if substring == "(":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break
      elif substring == ")":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

    # Validar si es llave
    substring=""
    for caracter in cadena:
      substring += caracter
      if substring == "{":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break
      elif substring == "}":
        simbolos.append(substring)
        tipo_de_simbolo.append(simbolos_lexicos[substring])
        matched = True
        break

    if matched == True:
      cadena = cadena[len(substring):].strip()
      matched = False
      pass

  
  return simbolos, tipo_de_simbolo

def construccionDeTabla(simbolos, tipo_de_simbolo):
  t = PrettyTable()
  t.add_column(column=simbolos, fieldname="SIMBOLO")
  t.add_column(column=tipo_de_simbolo, fieldname="TIPO")
  t.add_column(column=[tabla_de_simbolos[i] for i in tipo_de_simbolo], fieldname="NOMBRE")
  print(t)