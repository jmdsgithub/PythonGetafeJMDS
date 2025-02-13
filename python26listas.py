print("Listas con Python")
listaNumeros = [12,56,77,88,99,22]
#las listas comienzan en cero y finalizan en len
print("Número 0: ", listaNumeros[0])
print("Numero 1: ", listaNumeros[1])
listaNombres = ["Ana", "Lucas", "Adrian", "Antonia", "Lucas"]
print("Número 2: ", listaNombres[0])
print("Numero 4: ", listaNombres[1])
#append crea un nuevo elemnto en la liosta al final
listaNombres.append("Lucía")
print("Nombre 5: ", listaNombres[5])
#insert() crea un elemntonuevo en una posicion de la lisyta
listaNombres.insert(4, "Infiltrado")

listaNombres.remove("Ana")

listaNombres.pop(1)
del listaNombres[0:4]

listaNombres.clear()


for i in range(len(listaNombres)):
    print(str(i) + "=" + listaNombres[i])
