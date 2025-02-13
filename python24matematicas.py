#los imports se realizan de primero, antes de métodos y códigos lógicos
# from libreria24matematicas import sumarnumeros, restarNumeros
import libreria24matematicas

#codigo logico
print("Calculadora de métodos")
numero1 = 9
numero2 = 19
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0
if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(numero1, numero2)
elif (opcion == v2):
    resultado = libreria24matematicas.restarNumeros(numero1, numero2)
elif (opcion == 3):
    resultado = libreria24matematicas.multiplicarNumeros(numero1, numero2)
else:
    print("No ha seleccionadoi una opción correcta")
print("Resultado ", resultado)
print("Fin de programa")