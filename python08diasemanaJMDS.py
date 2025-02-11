print("Calcular día de la semana según año de nacimiento")
print("Introduzca el número de su día de nacimiento: ")
dia = int(input())
print("Introduzca el número de su mes de nacimiento: ")
mes = int(input())
print("Introduzca el número de su año de nacimiento")
ano = int(input())
if mes == 1:
    mes = 13
    ano = ano - 1
elif mes == 2:
    mes = 14
    ano = ano -1
#sabado = 0
#domingo = 1
#lunes = 2
#martes = 3
#miercoles = 4
#jueves = 5
#viernes = 6
from math import trunc
var1 = trunc((mes + 1) * 3)/5
var2 = trunc(ano / 4)
var3 = trunc(ano / 100)
var4 = trunc(ano / 400)
var5 = trunc(dia + (2 * mes) + ano + var1 + var2 - var3 + (var4 + 2))
var6 = trunc(var5 / 7)
var7 = trunc(var5 - (var6 * 7))
print("El día de la semana es: ")
if var7 == 0:
    print("Sábado")
elif var7 == 1:
    print("Domingo")
elif var7 == 2:
    print("Lunes")
elif var7 == 3:
    print("Martes")
elif var7 == 4:
    print("Miércoles")
elif var7 == 5:
    print("Jueves")
elif var7 == 6:
    print("Viernes")
print("Fin de programa")