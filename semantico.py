def validarSemantica(valores_por_regla):
  operaciones, asignaciones, definiciones = generarDiccionarios(valores_por_regla)
  errores = []
  print(operaciones, asignaciones, definiciones)
  # Operaciones
  for signo in operaciones:
    tipo_variable_anterior = ""
    for variable in operaciones[signo]:
      try:
        valor_de_variable = asignaciones[variable]

        try:
          tipo_de_variable = definiciones[variable]
          
          if tipo_de_variable == "float":
            if not isfloat(valor_de_variable):
              errores.append("Variable ({}) es del tipo ({}) pero se le quiere asignar el valor ({}).".format(variable, tipo_de_variable, valor_de_variable))
          elif tipo_de_variable == "int":
            if not isint(valor_de_variable):
              errores.append("Variable ({}) es del tipo ({}) pero se le quiere asignar el valor ({}).".format(variable, tipo_de_variable, valor_de_variable))

        except KeyError:
          errores.append("Variable ({}) no ha sido definida.".format(variable))
         
      except KeyError:
        errores.append("Variable ({}) no tiene asignación.".format(variable))

      try:
        if tipo_variable_anterior == "":
          tipo_variable_anterior = tipo_de_variable
        else:
          if tipo_variable_anterior != tipo_de_variable and signo in ["+", "-"]:
            errores.append("Variable tipo {} no se puede sumar o restar con variable tipo {}".format(tipo_variable_anterior, tipo_de_variable))
      except:
        continue

  if len(errores):
    for error in errores:
      print(error)
  else:
    print("No hay errores.")


def generarDiccionarios(valores_por_regla):
  variables_definidas = {}
  asignaciones_a_variables = {}
  operaciones_de_variables = {}
  
  for idx, valores in enumerate(valores_por_regla):
    if idx == len(valores_por_regla)-1:
      break

    # Definiciones
    if valores_por_regla[idx+1] == ["DefVar"] and valores[0] in ["int", "float", "cadena"]:
      #                  NOMBRE DE VAR  TIPO DE VAR
      variables_definidas[valores[1]] = valores[0]

    # Asignaciones
    if valores_por_regla[idx+1] == ["Sentencia"] and valores[1] == "=" and valores_por_regla[idx-1] == ["Termino"]:
      #                         NOMBRE DE VAR        VALOR ASIGNADO
      asignaciones_a_variables[valores[0]] = valores_por_regla[idx-2][0]
    elif valores_por_regla[idx+1] == ["Sentencia"] and valores[1] == "=" and valores_por_regla[idx-1][1] in ["+", "-", "/", "*"]:
      #                         NOMBRE DE VAR        VALOR ASIGNADO
      asignaciones_a_variables[valores[0]] = [valores_por_regla[idx-3][0], valores_por_regla[idx-5][0]]

    # Operaciones
    try:
      if valores[0] == "Expresion" and valores[1] in ["+", "-", "*", "/"] and valores[2] == "Expresion":
        #                         SIGNO               VAR 1                       VAR 2
        operaciones_de_variables[valores[1]] = [valores_por_regla[idx-2][0], valores_por_regla[idx-4][0]]
    except:
      continue
    
  return [variables_definidas, asignaciones_a_variables, operaciones_de_variables][::-1]

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True
