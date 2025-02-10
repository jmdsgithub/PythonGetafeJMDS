





km = int(input())
horasextra = 0
salarioextra = 0
salariobase = 0
salariototal = 0
dietas = ""
retencion = ""
#preguntamos si tenemois horas extras
if (horas trabajadas > 36):
    #horas extras
    horasextra = horastrabajadas - 36
    salariobase = preciohora * 36
    salarioextra = horasextra * (preciohora +2)
else:
    #no ha hecho horas extra
    horasextra = 0
    salarioextra = 0
    salariobase = horastrabajadas * preciohora
salariototal = salariobase + salarioextra
if (km <= 100):
    dietas = "LOCALES"
elif (km >= 101 and km <=500):
    dietas = "PROVINCIALES"
else:
    dietas = nacionales
if (salariototal < 250)
    retencion = "SIN RETENCION"
elif (salariototal >= 250 and salariototal <= 600)




print("Informe salario")
print("Horas trabajadas", horastrabajadas)
print("Horas extra ", horasextra)
print( 
print("Precio extra ", (preciohora + 2))
print("Salario base ", salariobase)
print()