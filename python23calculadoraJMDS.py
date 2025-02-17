def sumarN(num1, num2):
    return num1 + num2

def restarN(num1, num2):
    return num1 - num2

def multiplicarN(num1, num2):
    return num1 * num2

def dividirN (num1,num2):
    return num1 / num2

def mostrarMenu():
    print("Seleccione una de las siguientes operaciones: ")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")

    #programa principal
print("Operaciones")
print("Introduzca un número: ")
numA = int(input())
print("Introduzca otro número: ")
numB = int(input())
mostrarMenu()
opcion = int(input())
resultado = 0
if (opcion == 1):
    resultado = sumarN(numA, numB)
elif (opcion == 2):
    resultado = restarN(numA, numB)
elif (opcion == 3):
    resultado = multiplicarN(numA, numB)
else:
    (opcion == 4)
    resultado = dividirN(numA, numB)
print("El resultado es= ", resultado)
print("Fin de programa")