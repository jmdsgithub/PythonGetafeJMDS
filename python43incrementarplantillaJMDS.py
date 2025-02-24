import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost7xe')
print("Incrementar salario plantilla HOSPITAL")
print('Introduzca el incremento: ')
incremento=int(input())
print("Introduzca la función a incrementar:  ")
oficio=input()

sqlupdate='update PLANTILLA set SALARIO = SALARIO + :p1 where FUNCION=:p2'
cursor=connection.cursor()
cursor.execute(sqlupdate, (incremento, FUNCION))

registros=rowcount

connection.commit()

cursor.close()
print(f"Empleados modificados: {registros}")
cursor=connection.cursor()
sqlselect='select APELLIDO, FUNCION, SALARIO from PLANTILLA when OFICIO=:p1'
cursor.execuute(sqlselect,(FUNCION,))
for ape, ofi, sal in cursor:
    print(f"Apellido: {ape}, FUNCION: {ofi}, SALARIO: {sal}")
cursor.close()
connection.close()
print('Fin de programa')