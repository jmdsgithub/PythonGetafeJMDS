import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Insertar doctor en hospital')
print('Introduzca el APELLIDO del DOCTOR: ')
apellido=input()
print('Introduzca una especialidad: ')
especialidad=input()
print('Introduzca un salario: ')
salario=int(input())

sqlhospitales='select HOSPITAL_COD, NOMBRE from HOSPITAL'
cursor= connection.cursor()
cursor.execute(sqlhospitales)
contador=1
listahospitales=[]
for row in cursor:
    listahospitales.append (row[0])
    print (f'{contador} - {row [1]}')
    contador+= 1
cursor.close()
print('Seleccione un hospital: ')
opcion=int(input()) -1
idhospital=listahospitales[opcion]
