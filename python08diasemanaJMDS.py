print("Calcular dia de la semana")
print("Introduzca el número de su dia de nacimiento: ")
dia = int(input())
print("Introduzca el número de su mes de nacimiento: ")
mes = int(input())
print("Introduzca el número de su año de nacimiento")
ano = int(input())
#sabado = 0
#domingo = 1
#lunes = 2
#martes = 3
#miercoles = 4
#jueves = 5
#viernes = 6
var1 = ((mes + 1) * 3)/5
var2 = (ano / 4)
var3 = (ano/100)
var4 = (ano / 400)
var5 = (dia + (2* mes) + ano + var1 + var2 - var3 + (var4 + 2))
var6 = (var5 / 7)
var7 = (var5 - (var6 * 7))
print(str(var7))