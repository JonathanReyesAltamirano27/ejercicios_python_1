word = input('Ingresa una palabra: ')

if word == word[::-1]:
    print('No es un palíndromo!')
else:
    print('Es un palíndromo!')
    