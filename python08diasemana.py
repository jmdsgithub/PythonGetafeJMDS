from math import trunc
print("Día de nacimiento de la semana")
#los datos son numeros debemos convertir
#lo que el ususuario esta escribiendo
print("Introduzca el día: ")
dia = int(input())
print("Introduzca mes: ")
mes = int(input())
print("Introduzca año: ")
anyo = int(input())
if (mes == 1):
    mes = 13
    anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
op1 = trunc(((mes+1)*3)/5)
op2 = trunc(anyo / 4)
op3 = trunc(anyo / 100)
op4 = trunc(anyo / 400)
#
#
#
op5 = trunc(dia  + (mes*2) + anyo + op1 + op2 - op3 + op4 + 2)
op6 = trunc(op5 / 7)
resultado = trunc(op5 - (op6 * 7))
print("El día de la semana es: ")
if resultado == 0:
    print("Sábado")
elif resultado == 1:
    print("Domingo")
elif resultado == 2:
    print("Lunes")
elif resultado == 3:
    print("Martes")
elif resultado == 4:
    print("Miércoles")
elif resultado == 5:
    print("Jueves")
elif resultado == 6:
    print("Viernes")
print("Fin de programa")