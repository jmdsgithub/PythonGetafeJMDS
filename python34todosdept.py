import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

sql='select * from dept'
cursor=connection.cursor()
cursor.execute(sql)

for numero, nombre, localidad in cursor:
    print(str(numero) + ": " + nombre + ", " + localidad)

cursor.close()
connection.close()

#DEBEMOS CERRAR Y VOLVER A ABRIR LA CONEXION


connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql='select * from dept'
cursor=connection.cursor()
cursor.execute(sql)


# ********IMPORTANTE********regla de memoria para ITERACIONES ===== "FOR objeto IN conjunto"

for row in cursor:
    print (row)

    print(row[0])
    print(row[2])

fila=cursor.fetchone()
print(fila)
cursor.close()
connection.close()

print('Fin de BBDD')


