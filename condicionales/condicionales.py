# Estructura de Control if
# if else elif

'''
if exp_booleana:
instrucciones

if exp_booleana:
	instrucciones
else:
	instrucciones

if exp_bool:
	instrucciones
elif exp_bool:
	instrucciones
else:
	instrucciones:
'''

numero = int(input('Escribe un número: '))

if numero > 0:
	print("Es un número positivo")
elif numero < 0:
	print('El número 0')
else:
	print('Es un número negativo')
__