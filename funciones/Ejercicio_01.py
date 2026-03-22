# Procedimiento centrar: Recibe una cadena y la imprime centrada en la pantalla.
# Suponemos que tenemos una pantalla de 80 caracteres de ancho. 
# Para centrar usamos la formula 40 - (Longitud(cad)/2)
# Parámetros de entrada: cadena a imprimir centrada 

def centrar(frase):
    spaces = ' ' * (40 - len(frase) // 2)
    line = '=' * len(frase)

    print(spaces + frase)
    print(spaces + line)

if __name__ == '__main__':
   message_1 = input('Escribe una frase: ')
   message_2 = input('Escribe otra frase: ')
   print()
   centrar(message_1)
   centrar(message_2)

