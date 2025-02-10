print("Ejemplo mayor tres números")
print("Introduzca número 1: ")
numero1 = int(input())
print("Introduzca número 2: ")
numero2 = int(input())
print("Introduzca número 3: ")
numero3 = int(input())
mayor = 0
menor = 0
intermedio = 0
#comparamos cada número con los otros dos
if (numero1 >= numero2 and numero1 >= numero3):
    mayor = numero1
elif (numero2 >= numero1 and numero2 >= numero3):
    mayor = numero2
else:
    mayor = numero3
#misma pregunta pero camvbiando a numero menor
if (numero1 <= numero2 and numero1 <= numero3):
    menor = numero1
elif (numero2 <= numero1 and numero2 <= numero3):
    menor = numero2
else:
    menor = numero3
suma = numero1 + numero2 + numero3
intermedio  = suma - mayor - menor
print("Mayor: ", mayor)
print("Menor ", menor)
print("Intermedio ", intermedio)
print("Fin de programa")