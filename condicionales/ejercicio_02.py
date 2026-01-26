# Pedir un número y decir si es positivo, Negativo o 0 

numero = int(input('Ingresa un número: '))

if numero == 0:
	print('El número es Cero')
else:
	if numero > 0:
		print('El número es Positivo')
	else: 
		print('El número es Negativo')