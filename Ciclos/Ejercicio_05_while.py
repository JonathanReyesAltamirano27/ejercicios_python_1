
character = input('Escribe una letra (" " para salir): ')

while character != " ":
    if len(character) == 1:
        if character.upper() == 'A' \
        or character.upper() == 'E' \
        or character.upper() == 'I' \
        or character.upper() == 'O' \
        or character.upper() == 'U':
            print('Vocal')
        else:
            # Si es de longitud 1 y no es vocal, asumimos que es consonante
            print('Consonante')
    else:
        # Qué hacer si el usuario introduce más de una letra
        print('Por favor, ingresa solo una letra.')
        
    # Volvemos a pedir el input para que el ciclo avance y no sea infinito
    character = input('Escribe una letra (" P" para salir): ')

print("Programa terminado.")