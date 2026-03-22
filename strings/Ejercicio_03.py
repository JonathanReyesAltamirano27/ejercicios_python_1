cadena = input('Ingresa una frase: ')
caracter = input('Ingresa una letra: ')

repetidas = 0
for i in cadena:
    if i == caracter:
        repetidas += 1

print(f'La letra "{caracter}" se repite {repetidas} veces en la frase "{cadena}".')
