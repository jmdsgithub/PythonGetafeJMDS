def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs " + nombre)

def despedirse(nombre, dia):
    print("Un placer hoy " + dia + "Mr/Mrs " + nombre)

#-------------------------------------
print("Métodos con parámetros")
name = "Alumno "
dia = "miércoles "
saludar (name)
despedirse("jueves ", dia)

nom="Paco"
mes="diciembre"
saludar(nom)
despedirse(mes,"enero ")

print("Fin de programa")