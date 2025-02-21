#importamos la libreria de python oracle

import oracledb

#tenemos un objeto connection(user, pasword, server)

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

sql = "select * from dept"

cursor=connection.cursor()
cursor.execute(sql)

row=cursor.fetchone()
print(row)

row=cursor.fetchone()
print(row)

row=cursor.fetchone()
print(row)

row=cursor.fetchone()
print(row)

row=cursor.fetchone()
print(row)

print("Aún conectados!!!")

cursor.close()
connection.close()

print("Fin BBDD, desconectados!!!")
