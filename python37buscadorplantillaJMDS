import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Conectado a BBDD')

print('Buscador de empleados de plantilla por turno')
print('Introduzca el turno a consultar (M, T, N):')
data=input()
cursor=connection.cursor()
sql= 'Select * from plantilla where TURNO=' + data

cursor.execute(sql)

row=cursor.fetchone()

if (not row):
    print('No existe el turno')
else:
    apellido = row[3]
    direccion=row[4]
    turno=row[5]
    print("Apellido: " + apellido + ', ' + "Función: " + funcion + 'Turno: ' + turno)

cursor.close()
connection.close()
print('Fin de BBDD')