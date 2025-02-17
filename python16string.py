print("Clase string y funciones")
texto = "primero python"
#vamos probando metodos y viendo que devuelven
print("upper ", texto.upper())
print("replace " + texto.replace("o", "@"))
print("Letra 0:", texto[0])
print("Longitud (len)", len(texto))
print("find p: ", texto.find("p"))
print("Find Z:", texto.find("z"))
#sobrecarga de find (contenido a buscar, indice)
print("find p sobrecarga: ", texto.find("p", 1))
print("rfind ", texto.rfind("p"))
print("startswith A ", texto.startswith("A"))
print("endwith n ", texto.endswith("n"))
print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum())
# Vamos a visualizar que pasa con SLICING
# SUBSTRING
# QUEREMOS RECUPERAR DESDE LA POSICION 2 EN ADELANTE
substring = texto[2:]
print("Posicion 2 en adelante ", substring)
# EN PYTHON PODEMOS RECUPERAR UNA SUBCADENA
# DESDE UNA POSICION (2) A OTRA POSICION (5)
subtexto = texto[2: 5]
print("texto[2: 5] ", subtexto)
# PODEMOS RECORRER CADA CARACTER DE UN TEXTO
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("Posición " + str(i) + ": " + letra)
#podemos comprobar que el usuario ha escrito numeros o no
print("Introduzca un número: ")
#primero una variable auxiliar
aux = input()
if (aux.isdigit()):
    print("Esto es un número !!!")
else:
    print("No me has dado un número, campeón...")
print("Fin de programa")