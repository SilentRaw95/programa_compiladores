def convertir(i):
  if i == 0:
    return "0"
  s = ''
  while i:
    if i & 1 == 1:
      s = "1" + s
    else:
      s = "0" + s
    i //= 2
  return s

isbinary = False
palabra = raw_input("Ingresa una palabra: ")

for letra in palabra:
  if(int(letra) == 1 or int(letra) == 0):
    isbinary = True
  else:
    valor = ord(letra)
    temp = convertir(valor)
    print(str(valor)+" "+str(letra)+" = "+str(temp))
    

if(isbinary):
  valor = int(palabra, 2)
  temp = chr(valor)
  print(str(valor)+" "+str(palabra)+" = "+str(temp))