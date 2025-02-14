print("Rango de números pares")
print("Introduzca un número de inicio:")
inicio = int(input())
print("Introduzca un número de finalización:")
fin = int(input())
for i in range (inicio, fin, +1):
    #preguntamos si ekl numero es par
    if (i % 2 == 0):
        print (i)
print("Fin de programa")