import oracledb


print('Conectado a BBDD')

print('Buscador de empleados de plantilla por turno')
print('Introduzca el turno a consultar (M, T, N):')
data=input()

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor=connection.cursor()
sql= "Select APELLIDO, FUNCION from PLANTILLA where TURNO='" + data + "'"

print(sql)

cursor.execute(sql)

row=cursor.fetchone()

for APELLIDO, FUNCION in cursor:
    print('No existe el turno')
else:
    apellido = row[3]
    direccion=row[4]
    turno=row[5]
    print("Apellido: " + apellido + ', ' + "Función: " + funcion + 'Turno: ' + turno)

cursor.close()
connection.close()
print('Fin de BBDD')
