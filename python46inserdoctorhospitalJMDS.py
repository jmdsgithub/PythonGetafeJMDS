import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Insertar doctor en hospital')
print('Hospitales disponibles')
sqlhospitales='select HOSPITAL_COD, NOMBRE from HOSPITAL'
cursor= connection.cursor()
cursor.execute(sqlhospitales)
contador=1
listahospitales=[]
for row in cursor:
    print (f'{contador} - {row [0]}')
    listahospitales.append (row[0])
    contador=contador + 1
cursor.close()

print('Seleccione un hospital: ')
hospitalopcion=int(input())
opcion=listahospitales[opcion-1]
print('Introduzca el APELLIDO del DOCTOR: ')
apellido=input()
print('Introduzca una especialidad: ')
especialidad=input()
print('Introduzca un salario: ')
salario=int(input())

sqldoctores=


























connection.close()
print('Fin de programa')