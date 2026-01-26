# Programa que es valide usuario y contraseña

user = 'admin'
password = 'qwerty'

usuario = input('Ingresa tu Usuario:')
contra = input('Ingresa tu contraseña:')

if user == usuario and password == contra:
	print('Has encontrado al Sistema')
else:
	print('Error de Acceso')