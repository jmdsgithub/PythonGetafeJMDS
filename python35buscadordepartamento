import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Conectado a BBDD')

print('Introduzca número de departamento:')
data=input()
cursor=connection.cursor()
sql= 'Select * from dept where dept_no=' + data

cursor.execute(sql)

row=cursor.fetchone()

if (not row):
    print('No existe el dpto')
else:
    nombre = row[1]
    localidad=row[2]
    print(nombre + ', ' + localidad)

cursor.close()
connection.close()
print('Fin de BBDD')
