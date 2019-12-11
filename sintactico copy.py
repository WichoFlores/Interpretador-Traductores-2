import pandas as pd
from lexico import simbolos_lexicos, tabla_de_simbolos
from prettytable import PrettyTable

# Reducciones

# Leer y limpiar .csv

reducciones = {
    1: 24,
    2: 25,
    3: 25,
    4: 26,
    5: 26,
    6: 27,
    7: 28,
    8: 28,
    9: 29,
    10: 30,
    11: 30,
    12: 31,
    13: 31,
    14: 32,
    15: 33,
    16: 33,
    17: 34,
    18: 34,
    19: 35,
    20: 35,
    21: 36,
    22: 36,
    23: 36,
    24: 36,
    25: 36,
    26: 37,
    27: 37,
    28: 38,
    29: 39,
    30: 39,
    31: 40,
    32: 40,
    33: 41,
    34: 41,
    35: 42,
    36: 42,
    37: 42,
    38: 42,
    39: 42,
    40: 43,
    41: 44,
    42: 44,
    43: 45,
    44: 45,
    45: 45,
    46: 45,
    47: 45,
    48: 45,
    49: 45,
    50: 45,
    51: 45,
    52: 45
}

simbolos_por_regla = {
  1: 1,
  2: 0,
  3: 2,
  4: 1,
  5: 1,
  6: 4,
  7: 0,
  8: 3,
  9: 6,
  10: 0,
  11: 3,
  12: 0,
  13: 4,
  14: 3,
  15: 0,
  16: 2,
  17: 1,
  18: 1,
  19: 0,
  20: 2,
  21: 4,
  22: 6,
  23: 5,
  24: 3,
  25: 2,
  26: 0,
  27: 2,
  28: 3,
  29: 0,
  30: 1,
  31: 0,
  32: 2,
  33: 0,
  34: 3,
  35: 1,
  36: 1,
  37: 1,
  38: 1,
  39: 1,
  40: 4,
  41: 1,
  42: 1,
  43: 3,
  44: 2,
  45: 2,
  46: 3,
  47: 3,
  48: 3,
  49: 3,
  50: 3,
  51: 3,
  52: 1

}


data = pd.read_csv("./resources/gramatica.csv")
data = data.drop(data.columns[[0]], axis=1)
data = data.replace(['d', 'r'], ['', '-'], regex=True)
data = data.fillna(0)
data = data.to_numpy()

def procesarSintaxis(entrada):
  pila = [simbolos_lexicos["$"], 0]
  entrada.append(simbolos_lexicos["$"])

  for idx, caracter in enumerate(entrada):
    fila = pila[-1]
    columna = caracter
    salida = int(data[fila][columna])

    # if salida == 0:
    #   mostrarTabla(pila, entrada[idx:], salida)
    #   return

    # 2 Pops por parámetro
    # si es negativo, es una reducción
    if salida < 0:
    
      mostrarTabla(pila, entrada[idx:], str("r{} ({} -> {})".format(abs(salida), tabla_de_simbolos[reducciones[abs(salida)]], salida-1)))
      # salida = abs(salida)
      print(tabla_de_simbolos[reducciones[abs(salida)]])

      simbolos = simbolos_por_regla[abs(salida)]
      print("Simbolos de la regla {}: {}".format(abs(salida), simbolos))
      for _ in range(0, simbolos):
        pila.pop()
        pila.pop()
      
      # Tipo de Reducción
      fila = pila[-1]
      columna = reducciones[abs(salida)]
      
      print("Reduciendo...")
      mostrarTabla(pila, [columna] + entrada[idx:], int(data[fila][columna]))
      pila.append(columna)
      pila.append(int(data[fila][columna]))

      fila = pila[-1]
      columna = caracter

      print("Reducido")
      mostrarTabla(pila, entrada[idx:], int(data[fila][columna]))

      pila.append(reducciones[abs(salida)])
      pila.append(int(data[fila][columna]))
      # pila.append(caracter)
      # pila.append(caracter)


    else:
      mostrarTabla(pila, entrada[idx:], salida)
      if caracter != 23:
        pila.append(caracter)
      if salida != 0:
        pila.append(salida)

    if len(entrada[idx+1:]) == 0:
      entrada.append(simbolos_lexicos["$"])
    input("")
  
  print(pila)

def mostrarTabla(pila, entrada, salida):
  t = PrettyTable()
  t.field_names = ["PILA", "ENTRADA", "SALIDA"]
  t.add_row([pila, entrada, salida])
  print(t)