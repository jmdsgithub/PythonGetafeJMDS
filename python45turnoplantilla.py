import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Buscador de EMPLEADOS de PLANTILLA por TURNO')
sqlturnos='''select distinct TURNO, case TURNO when 'T' then 'TARDE' when 'M' then 'MAÑANA' when 'N' then 'NOCHE' end as VALOR from PLANTILLA'''
cursor=connection.cursor()
cursor.execute(sqlturnos)
contador=1

listaturnos=[]
for row in cursor:
    print(f'{contador} - {row[1]}')
    listaturnos.append (row[1])
    contador+=1
cursor.close()

print('Selecciones una opción: ')
opcion=int(input())-1
turno=listaturnos[opcion]

sqlempleados='select * from PLANTILLA where TURNO=:p1'
cursor=connection.cursor()
cursor.execute(sqlempleados, (turno,))

for row in cursor:
    print (row )
cursor.close()
connection.close()
print('Fin de programa')



#hay que revisarlo que da error