# funciones de identificaciones
# indentificador aritmetico
def indf_aritmetico(palabra):
  if(palabra == '+'):
    return True
  elif(palabra == '-'):
    return True
  elif(palabra == '*'):
    return True
  elif(palabra == '/'):
    return True
  elif(palabra == '++'):
    return True
  elif(palabra == '--'):
    return True
  else:
    return False

# indentificador comparacion
def indf_comparacion(palabra):
  if(palabra == '>'):
    return True
  elif(palabra == '<'):
    return True
  elif(palabra == '>='):
    return True
  elif(palabra == '<='):
    return True
  elif(palabra == '=='):
    return True
  elif(palabra == '!='):
    return True
  else:
    return False

# indentificador logico
def indf_logico(palabra):
  if(palabra == '&&'):
    return True
  elif(palabra == '||'):
    return True
  elif(palabra == '!'):
    return True
  else:
    return False

# indentificador agrupacion
def indf_agrupacion(palabra):
  if(palabra == '('):
    return True
  elif(palabra == ')'):
    return True
  elif(palabra == '{'):
    return True
  elif(palabra == '}'):
    return True
  elif(palabra == '['):
    return True
  elif(palabra == '"'):
    return True
  elif(palabra == "'"):
    return True
  else:
    return False

# identificador numero
def indf_numero(palabra):
  try:
    val = int(palabra)
    return True
  except ValueError:
    return False

# identificador general
def indf_general(palabra):
  if(indf_aritmetico(palabra)): # puede tener 1 o 2 caracteres (casi terminado)
    return 'aritmetico'
  elif(indf_comparacion(palabra)): # puede tener 1 o 2 caracteres (casi terminado)
    return 'comparacion'
  elif(indf_logico(palabra)): # puede tener 1 o 2 caracteres (casi terminado)
    return 'logico'
  elif(indf_numero(palabra)): # puede ser n caracteres (terminado)
    return 'numero'
  elif(indf_agrupacion(palabra)): # debe ser de un caractere (terminado)
    return 'agrupacion'
  elif(palabra == ' '): # debe ser de 1 caracter (terminado)
    return 'espacio'
  elif(palabra == ';'): # debe ser de 1 caracter (terminado)
    return 'separador'
  elif(palabra == ''): # valores invalidos (terminado)
    return 'vacio'
  else: # puede ser n caracteres (terminado)
    return 'palabra'



# programa
while(True):
  oracion = raw_input("Ingresa una sentencia: ")

  # variables acumuladores, registros
  list_aritmeticos = []
  list_comparacion = []
  list_logicos = []
  list_agrupacion = []
  list_numeros = []
  list_palabras = []
  no_espacios = 0
  no_separadores = 0

  reg_palabra = ''
  reg_aritmetico = ''
  reg_comparacion = ''
  reg_logico = ''

  estado_palabra = ''

  long_oracion = len(oracion)

  # separacion de letras
  for letra in oracion:
    reg_palabra = reg_palabra + letra
    estado_palabra = 'completa'

    # ---------------------------------------------- aritmeticos seccion (terminada)
    if((indf_general(letra) == 'aritmetico' or len(reg_aritmetico) > 0) and estado_palabra != 'total'):
      reg_aritmetico = reg_aritmetico + letra

      if(len(reg_aritmetico) == 2):
        # obtener aritmeticos
        if(indf_general(reg_aritmetico) == 'aritmetico'):
          list_aritmeticos.append(reg_aritmetico)
          estado_palabra = 'total'
        else:
          list_aritmeticos.append(reg_aritmetico[0])
          estado_palabra = 'parcial'
        
        # separar palabra
        respaldo = ''
        reg_palabra = reg_palabra[:-2]
        
        if(estado_palabra == 'total'):
          reg_aritmetico = ''
        else:
          if(indf_general(reg_aritmetico[1]) == 'aritmetico'):
            respaldo = reg_aritmetico[1]
            reg_aritmetico = reg_aritmetico[1]
          else:
            respaldo = reg_aritmetico[1]
            reg_aritmetico = ''
        
        # asignar separacion
        if(indf_general(reg_palabra) == 'numero'):
          list_numeros.append(reg_palabra)
        elif (indf_general(reg_palabra) == 'palabra'):
          list_palabras.append(reg_palabra)
        
        reg_palabra = '' + respaldo

    # ---------------------------------------------- comparacion seccion (terminada)
    if((indf_general(letra) == 'comparacion' or len(reg_comparacion) > 0 or letra == '=') and estado_palabra != 'total'):
      reg_comparacion = reg_comparacion + letra

      if(len(reg_comparacion) == 2):
        # obtener aritmeticos
        if(indf_general(reg_comparacion) == 'comparacion'):
          list_aritmeticos.append(reg_comparacion)
          estado_palabra = 'total'
        else:
          list_aritmeticos.append(reg_comparacion[0])
          estado_palabra = 'parcial'
        
        # separar palabra
        respaldo = ''
        reg_palabra = reg_palabra[:-2]
        
        if(estado_palabra == 'total'):
          reg_comparacion = ''
        else:
          if(indf_general(reg_comparacion[1]) == 'comparacion'):
            respaldo = reg_comparacion[1]
            reg_comparacion = reg_comparacion[1]
          else:
            respaldo = reg_comparacion[1]
            reg_comparacion = ''
        
        # asignar separacion
        if(indf_general(reg_palabra) == 'numero'):
          list_numeros.append(reg_palabra)
        elif (indf_general(reg_palabra) == 'palabra'):
          list_palabras.append(reg_palabra)
        
        reg_palabra = '' + respaldo
    
    # ---------------------------------------------- logico seccion (progreso)
    if((indf_general(letra) == 'logico' or len(reg_logico) > 0 or letra == '&' or letra == '|') and estado_palabra != 'total'):
      reg_logico = reg_logico + letra

      if(len(reg_logico) == 2):
        # obtener aritmeticos
        if(indf_general(reg_logico) == 'logico'):
          list_logicos.append(reg_logico)
          estado_palabra = 'total'
        else:
          list_logicos.append(reg_logico[0])
          estado_palabra = 'parcial'
        
        # separar palabra
        respaldo = ''
        reg_palabra = reg_palabra[:-2]
        
        if(estado_palabra == 'total'):
          reg_logico = ''
        else:
          if(indf_general(reg_logico[1]) == 'logico'):
            respaldo = reg_logico[1]
            reg_logico = reg_logico[1]
          else:
            respaldo = reg_logico[1]
            reg_logico = ''
        
        # asignar separacion
        if(indf_general(reg_palabra) == 'numero'):
          list_numeros.append(reg_palabra)
        elif (indf_general(reg_palabra) == 'palabra'):
          list_palabras.append(reg_palabra)
        
        reg_palabra = '' + respaldo
    
    # ---------------------------------------------- agrupacion seccion (terminado)
    if((indf_general(letra) == 'agrupacion') and estado_palabra != 'total'):
      list_agrupacion.append(letra)

      reg_palabra = reg_palabra[:-1]

      # asignar separacion
      if(indf_general(reg_palabra) == 'numero'):
        list_numeros.append(reg_palabra)
      elif (indf_general(reg_palabra) == 'palabra'):
        list_palabras.append(reg_palabra)
      
      estado_palabra = 'total'
      reg_palabra = ''

    # ---------------------------------------------- espacio seccion (terminado)
    if((indf_general(letra) == 'espacio') and estado_palabra != 'total'):
      no_espacios = no_espacios + 1

      reg_palabra = reg_palabra[:-1]

      # asignar separacion
      if(indf_general(reg_palabra) == 'numero'):
        list_numeros.append(reg_palabra)
      elif (indf_general(reg_palabra) == 'palabra'):
        list_palabras.append(reg_palabra)
      
      estado_palabra = 'total'
      reg_palabra = ''

    # ---------------------------------------------- separador seccion (terminado)
    if((indf_general(letra) == 'separador') and estado_palabra != 'total'):
      no_separadores = no_separadores + 1

      reg_palabra = reg_palabra[:-1]

      # asignar separacion
      if(indf_general(reg_palabra) == 'numero'):
        list_numeros.append(reg_palabra)
      elif (indf_general(reg_palabra) == 'palabra'):
        list_palabras.append(reg_palabra)
      
      estado_palabra = 'total'
      reg_palabra = ''
      
  #cuando se acaba la iteracion
  if(len(reg_aritmetico) > 0):
    list_aritmeticos.append(reg_aritmetico)
  elif(len(reg_comparacion) > 0):
    list_comparacion.append(reg_comparacion)
  elif(len(reg_logico) > 0):
    list_logicos.append(reg_logico)
  elif(indf_general(reg_palabra) == 'numero'):
    list_numeros.append(reg_palabra)
  elif(indf_general(reg_palabra) == 'palabra'):
    list_palabras.append(reg_palabra)

  # mostrar datos
  if(len(list_aritmeticos) > 0):
    print('')
    print('Aritmeticos')
    for item in list_aritmeticos:
      print(item)
  
  if(len(list_comparacion) > 0):
    print('')
    print('Comparacion')
    for item in list_comparacion:
      print(item)
  
  if(len(list_logicos) > 0):
    print('')
    print('Logicos')
    for item in list_logicos:
      print(item)
  
  if(len(list_agrupacion) > 0):
    print('')
    print('Agrupacion')
    for item in list_agrupacion:
      print(item)
  
  if(len(list_numeros) > 0):
    print('')
    print('Numeros')
    for item in list_numeros:
      print(item)

  if(len(list_palabras) > 0):
    print('')
    print('Palabras')
    for item in list_palabras:
      print(item)
  
  if(no_espacios > 0):
    print('')
    print('No. de espacios: '+str(no_espacios))
  
  if(no_separadores > 0):
    print('')
    print('No. de (;): '+str(no_separadores))
  
  print('')
    