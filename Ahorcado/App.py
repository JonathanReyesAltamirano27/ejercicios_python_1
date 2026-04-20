import random

# Menú para elegir archivo
def select_file():
    print('=== "Bienbenido al juego del ahorcado" ===')
    print('==========================================')
    print("📂 Selecciona una categoría:")
    print("1. Comidas")
    print("2. Deportes")
    print("3. Géneros musicales")
    print("4. Materias")
    print("5. Países")

    while True:
        option = input("Elige una opción (1-5): ")

        match option:
            case "1":
                return 'comidas.txt'
            case "2":
                return 'Deportes.txt'
            case "3":
                return 'Generos.musicales.txt'
            case "4":
                return 'Materias.txt'
            case "5":
                return 'Paises.txt'
            case _:
                print("❌ Opción inválida, intenta de nuevo")


# Obtener palabra
def get_word():
    archivo = select_file()

    with open(archivo, 'r', encoding='utf-8') as f:
        words = f.read().split('\n')

    return random.choice(words).lower()


# Dibujar ahorcado
def draw(errors):
    match(errors):
        case 0:
            ahorcado = '''
    |-----------------------
    |          
    |          
    |         
    |         
    |_______________________
   '''
        case 1:
            ahorcado = '''
    |-----------------------
    |          |
    |          
    |        
    |         
    |_______________________    
    '''
        case 2:
            ahorcado = '''
    |-----------------------
    |          |
    |          O
    |         
    |         
    |_______________________   
    '''
        case 3:
            ahorcado = '''
    |-----------------------
    |          |
    |          O
    |         /|\\
    |         
    |_______________________    
    '''
        case 4:
            ahorcado = '''
    |-----------------------
    |          |
    |          O
    |         /|\\
    |          |
    |         
    |_______________________    
    '''
        case 5:
            ahorcado = '''
    |-----------------------
    |          |
    |          O
    |         /|\\
    |          |
    |         / \\
    |_______________________     
    '''
        case _:
            ahorcado = ''
    print(ahorcado)


# Mostrar palabra
def write_word(word, chars=''):
    dashed_word = '_ ' * len(word)
    for char in chars:
        new_word = ''
        for i in range(len(word)):
            if char == word[i]:
                new_word += char + ' '
            else:
                new_word += dashed_word[i * 2 : i * 2 + 2]
        dashed_word = new_word
    return dashed_word


# Juego
def game():
    word = get_word()

    print("\n🎮 Iniciemos 🎮")
    print(write_word(word))

    errors = 0
    chars = ''

    while True:
        char = input('Ingresa una letra o la palabra: ').lower()

        if len(char) == 1 and char.isalpha():
            if char not in word:
                errors += 1
                draw(errors) 
            else:
                print("✅ Letra correcta")

            chars += char
            dashed_word = write_word(word, chars)
            print(dashed_word)

            if dashed_word.replace(' ', '') == word:
                print("🎉 Ganaste ¡Wahoo!")
                break
        else:
            print("❌ Entrada inválida, Waaaaa!")

        if errors == 6:
            print("💀 JAJA Perdiste, Mamma mia!")
            print(f"La palabra era: {word}")
            break


# Ejecutar
if __name__ == "__main__":
    game()