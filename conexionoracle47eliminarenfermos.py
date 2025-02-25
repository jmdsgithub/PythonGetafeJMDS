import oracledb

class ConexionOracleEnfermos:



    def __init__ (self):
        self.connection=oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    
    def eliminarEnfermo(self, inscripcion):
        cursor=self.connection.cursor()
        sql='delete from ENFERMO where INSCRIPCION=:p1'
        cursor.execute(sql, (inscripcion,))
        registros=cursor.rowcount
        cursor.close()
        return registros
    
    def modificarEnfermo(self, apellido, inscripcion):
        cursor=self.connection.cursor()
        sql='update ENFERMO set APELLIDO=:p1 where INSCRIPCION=:p2'
        cursor.execute(sql, (apellido, inscripcion))
        registros=cursor.rowcount
        cursor.close()
        return registros

