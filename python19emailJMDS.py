print("Validar e-mail")
print("Introduzca un email")
email = input()
if email.count("@") ==1:
    print("El email solo debe contener una @")
elif email.count(".") ==1:
    print("El email solo debe contener un punto")
elif email.startswith("@"):
    print("El email no puede empezar con @")
elif email.endswith("@"):
    print("El email no debe terminar con @")
elif email.startswith("."):
    print("El email no debe empezar con un punto")
elif email.endswith("."):
    print("El email no debe terminar con un punto")
else: 
    print("El email es válido")
print("Fin de programa")