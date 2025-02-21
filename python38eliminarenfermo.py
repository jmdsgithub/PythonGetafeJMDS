import oracledb
print("Eliminar inscripción de enfermo")
print("Introduzca número de inscripción de enfermo a borrar: ")
data=input()
sql= "delete from ENFERMO where INSCRIPCION=" + data


connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor=connection.cursor()



cursor.execute(sql)
afectados=cursor.rowcount
connection.commit()
print("Registros eliminados: " + str(afectados))
cursor.close()
connection.close()
print("Fin de programa y cierre de BBDD")