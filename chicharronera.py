import math
val_a = raw_input("Ingresa el valor de (A): ") # 4
val_b = raw_input("Ingresa el valor de (B): ") # 9
val_c = raw_input("Ingresa el valor de (C): ") # 2

raiz = math.sqrt( (float(val_b)**2) - (4* float(val_a) * float(val_c) ) )
re_positivo = ( (-float(val_b)) + raiz) / ( 2* float(val_a))
re_negativo = ( (-float(val_b)) - raiz) / ( 2* float(val_a))

print('x1: ',re_positivo,' x2: ',re_negativo)