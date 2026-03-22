# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = input('Escribe algo:\n')
subcadena = input('Escribe una subcadena: \n')

if cadena.startswith(subcadena):
    print(cadena, 'Si comienza con', subcadena)
else:
    print(cadena, 'No comienza con', subcadena)
    