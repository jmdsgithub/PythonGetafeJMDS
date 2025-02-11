print("Tabla de multiplicar")
print("Introduzca un número")
numero = int(input())
for i in range (0,11):
    resultado = i * numero
    print(("%d x %d = %d")%(numero, i, resultado))
print("Final de programa")