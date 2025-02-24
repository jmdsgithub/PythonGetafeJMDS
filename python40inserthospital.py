import oracledb
print('Insertar HOSPITALES BBDD')

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print('Introduzca un ID HOSPITAL')
iddept=input()
print('Introduzca nombre')
nombre=input()
print('Introduzca localidad')
localidad=input()




#insert into HOSPITAL values (11, 'name', 'tlfn','camas')
sqlinsert= "insert into HOSPITAL values"
print (sqlinsert)