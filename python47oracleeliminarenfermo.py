from conexionoracle47eliminarenfermos import ConexionOracleEnfermos

print('Probando clases de oracle: ENFERMOS: ')
print('Introduzca una inscripción update: ')
inscripcion=int(input())
print('Introduzca un nuevo apellido: ')
apellido=input()
connection=ConexionOracleEnfermos()
modificados=connection.modificarEnfermo(apellido, inscripcion)
print(f'Enfermos modificados: {modificados}')
print('Fin de programa')