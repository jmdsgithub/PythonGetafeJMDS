print("Calcular salario trabajadores")
print("Introduzca el numero de horas trabajadas: ")
horastrabajadas = int(input())
print("Introduzca el precio hora: ")
preciohora = int(input())
print("Introduzca los kilometros recorridos: ")
kmsrecorridos = int(input())
salariobase = 0
#Calculo salario
if (horastrabajadas > 36):
    salarioextra = ((preciohora +2) * (horastrabajadas-36))
    salariobase = 36 * preciohora
else:
    salarioextra=0
    salariobase = horastrabajadas * preciohora
salariototal = salariobase + salarioextra
print("El salario total es: ", salariototal)
