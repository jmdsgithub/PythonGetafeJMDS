print("Calcular salario trabajadores")
print("Introduzca el numero de horas trabajadas: ")
horastrabajadas = int(input())
print("Introduzca el precio hora base: ")
preciohorabase = int(input())
print("Introduzca el precio hora extra: ")
preciohoraextra = int(input())
print("Introduzca los kilómetros recorridos: ")
kmsrecorridos = int(input())
#Calculo salario
if (horastrabajadas <= 36):
    salariobase = (preciohorabase * horastrabajadas)
elif (horastrabajadas > 36):
    salarioextra = (preciohoraextra * horastrabajadas)
salariototal = salariobase + salarioextra
print("El salario tiotal es: ", salariototal)