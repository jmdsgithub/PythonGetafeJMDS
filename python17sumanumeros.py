print("Suma números texto string")
print("Introduzca un texto numerico ")
textonumeros = input()
suma = 0
longitud = len(textonumeros)
#recorremos cada letra del texto
for i in range(longitud):
    #almacenamos cada letra de cada posicion
    letra = textonumeros[i]
    #convertimos cada letra a entero
    numero = int(letra)
    #sumamos cada numero
    suma = suma + numero
print("La suma de " + textonumeros + " es " + str(suma))
print("Fin de programa")


print("Suma de digitos")
sumadedigitos=input("Introduzca un numero de varios digitos: ")
suma=0

for cadadigito in range (len(sumadedigitos)):
    letranum=sumadedigitos[cadadigito]
    num=int(letranum)
    suma=suma+num
print("La suma de los digitos es: ", suma)
print("Fin de programa")