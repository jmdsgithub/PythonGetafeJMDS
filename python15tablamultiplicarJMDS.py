print("Tabla de multiplicar")
print("Introduzca un número")
numero = int(input())
for i in range (0,11):
    resultado = i * numero
    print(str(numero), "*", str(i), "=", int(resultado))
print("Final de programa")


factor1=(int(input("Introduzca un factor: ")))
                                           
for factor2 in range(0,11):
    resultado=factor2*factor1
    print(str(factor1), " * ", str(factor2), " = ", int(resultado))