#Es un programa que deseamos ejecutar
#los métodos se declaran al inicio
#la sintaxis de nombres de métodos es:
# primeraSegundaTercera
def primerMetodo():
    #este codigo nunca se ejecutará
    #si no lo llamamos de forma explicita
    print("Soy el primer método")
def segundoMetodo():
    print("Segundo método")

#Aquí tenemos el código principal
print("Ejemplo de métodos")
#podemos llamar al metodo si lo deseamos
primerMetodo()
segundoMetodo()
primerMetodo()
print("Fin de programa")