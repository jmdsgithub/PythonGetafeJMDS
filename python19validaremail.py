print("Validación email")
print("Introduzca un email")
email = input()
#email con @
if (email.count("@") == 0):
    print("Email sin @")
#que exista un punto
elif (email.find(".") == -1):
    print("Email sin punto")
#email sin @ al inicio o al final
elif(email.startswith("@") == True or email.endswith("@") == True):
    print("@ al inicio o al final del email")
#email sin "." al inicio o al final
elif(email.startswith(".") == True or email.endswith(".") == True):
    print(". al inicio o al final del email")
#email con una sola @
elif (email.count("@") > 1):
    print("Existe más de una @")
#exista punto despues de arroba
elif (email.find("@") > email.rfind(".")):
    print("Debe existir un punto después de la @")
else:
    #Necesitamos recuperar el dominio
    ultimopunto = email.rfind(".")
    # recuoeramos el dominioi a partir del ultimo punto en adelante
    dominio = email[ultimopunto + 1:]
    #longitud del dominio
    longituddominio = len(dominio)
    #comprobar la longitud del dominio
    if (longituddominio >= 2 and longituddominio <= 3):
        print("Email correcto")
    else: print("El email debe tener un dominio de 2 a 3 caracteres")
print("Fin de programa")