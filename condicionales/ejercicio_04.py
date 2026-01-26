# Programa que hace una división
# Si el divisor es 0 que termine o que diga que no se puede 

num_1 = int(input('Ingresa un número:'))
num_2 = int(input('Ingresa otro número:'))

if num_2 == 0:
	print('No se puede dividir entre 0')
else:
	divi = num_1 / num_2
	print('La división es:', divi)