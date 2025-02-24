import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("INCREMENTAR SALARIO EMPLEADOS")
print("Introduzca incremento: ")
incremento=int(input())
print("Introduzca el oficio a incrementar: ")
oficio=input()

sqlupdate="update EMP set salario = SALARIO +  :p1 where OFICIO=:p2"
cursor=connection.cursor()
cursor.execute(sqlupdate, (incremento, oficio))
()
registros=cursor.rowcount

connetion.commit()

cursor.close()


sqlselect=?select APELLIDO, OFICOP, SALARIO from EMP



cursor.close()
connection.close()
print("Fin de programa y cierre de BBDD")


