import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Buscador de EMPLEADOS de PLANTILLA por TURNO')
sqlturnos='select distinct TURNO from PLANTILLA'
cursor=connection.cursor()
cursor.execute(sqlturnos)
contador=1

listaturnos=[]
for row in cursor:
    print(f'{contador} - {row[0]}')
    listaturnos.append (row[0])
    contador=contador+1
cursor.close()

print('Selecciones una opción: ')
opcion=int(input())
turno=listaturnos[opcion-1]

sqlempleados='select * from PLANTILLA where TURNO=:p1'
cursor=connection.cursor()
cursor.execute(sqlempleados, (turno,))

for row in cursor:
    print (row )
cursor.close()
connection.close()
print('Fin de programa')