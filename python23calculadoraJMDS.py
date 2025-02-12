def sumar(num1, num2):
    return num1 + num2 ()

def restar(num1, num2):
    return num1 - num2 ()

def concatenar(num1, num2):
    return num1 * num2

def mostrarMenu():
    print("Seleccione una de las siguientes operaciones: ")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")

    #programa principal
print("Operaciones")
print("Introduzca un número: ")
num1 = input()
print("Introduzca otro número: ")
num2 = input()
mostrarMenu()
opcion = int(input())
resultado = ""
if (opcion == 1):
    resultado = sumar(valor)
elif (opcion == 2):
    resultado = restar(valor)
else:
    (opcion == 3)
    resultado = multiplicar(valor)
print(resultado)
print("Fin de programa")