from clase32mes import Mes
import random

print("Trabajando con clase Mes ")
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for nombreMes in meses:
    print(nombreMes)
    mes = Mes ()
    mes.nombre = nombreMes
    mes.temperaturaMaxima = random.randint(1, 40)
    mes.temperaturaMinima = random.randint(1, 40)
    media = mes.getTemperaturaMedia ()
    print ("Media ", media)
    print(mes)
