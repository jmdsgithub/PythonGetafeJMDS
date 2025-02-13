from libreria25validaciones import validarISBN, validarDNI

print("Clase programa validaciones")
print("Introduzca ISBN")
isbn = input()
valido= validarISBN(isbn)
print("El ISBN es ", valido)
