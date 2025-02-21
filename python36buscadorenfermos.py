import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Conectado a BBDD')

print('Buscador de enfermos')
print('Introduzca número de inscripción:')
data=input()
cursor=connection.cursor()
sql= 'Select * from enfermo where inscripcion=' + data

cursor.execute(sql)

row=cursor.fetchone()

if (not row):
    print('No existe la inscripción')
else:
    apellido = row[1]
    direccion=row[2]
    print("Apellido: " + apellido + ', ' + "Dirección: " + direccion)

cursor.close()
connection.close()
print('Fin de BBDD')
