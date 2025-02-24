import oracledb
print("Ejemplo de parámetros Oracle")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Introduzca Número de departamento')
iddept=input()
sql=f'select*from EMP where DEPT_NO={iddept}'
print(sql)
cursor=connection.cursor()
cursor.execute(sql)

for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Departamento: {row[7]}")
cursor.close()
connection.close()
print("Fin de programa y cierre de BBDD")
