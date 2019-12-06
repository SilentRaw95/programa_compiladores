memoriamax = raw_input("Ingresa la cantida de memoria maxima: ")
memoria = raw_input("Ingresa la memoria de los procesos: ")
proceso = raw_input("Ingresa la cantidad de procesos: ")

res = int(memoria) * int(proceso)
total = int(memoriamax) - int(res)

print("Cantidad de memoria "+str(memoriamax))
print(str(proceso)+" proceso "+str(res)+"kb")