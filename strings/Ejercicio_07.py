frase = input('Ingresa una frase: ')


while True:
    letra_l = input('Ingresa una letra: ')
    if len(letra_l) == 1:
        break


while True:
    letra_2 = input('Ingresa una letra para sustituir la palabra: ')
    if len(letra_2) == 1:
        break
frase_nueva = ''
for letra in frase:
    if letra == letra_l:
        frase_nueva = frase_nueva + letra_2
    else:
        frase_nueva += letra

print('La frase nueva queda así:\n' + frase_nueva) 

frase_2 = frase.replace(letra_l, letra_2)
print('La frase nueva queda así:\n' + frase_2)  
