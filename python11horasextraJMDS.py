print("Calcular salario trabajadores")
print("Introduzca el numero de horas trabajadas: ")
horastrabajadas = int(input())
print("Introduzca el precio hora: ")
preciohora = int(input())
print("Introduzca los kilometros recorridos: ")
km = int(input())
salariobase = 0
#Calculo salario
if (horastrabajadas > 36):
    salarioextra = ((preciohora +2) * (horastrabajadas-36))
    salariobase = preciohora * 36
else:
    salarioextra=0
    horasextra=0
    salariobase = horastrabajadas * preciohora
salariototal = salariobase + salarioextra
if (km <= 100):
    dietas = "LOCALES"
elif (km >= 101 and km <=500):
    dietas = "PROVINCIALES"
else:
    dietas = "NACIONALES"
if (salariototal < 250):
    retencion = "SIN RETENCION"
elif (salariototal >= 250 and salariototal <= 600):
    retencion = "20% de retención"
else:
    retencion = "40% de retención"
#INFORME
print("Informe salario ")
print("Horas trabajadas: ", horastrabajadas)
print("Horas extra: ", horasextra)
print("Precio hora: ", preciohora)
print("Precio extra: ", (preciohora + 2))
print("Salario base: ", salariobase)
print("Salario extra: ", salarioextra)
print("Salario total ", salariototal)
print("Retenciones: ", retencion)
print("Dietas: ", dietas)
print("Fin de programa.")