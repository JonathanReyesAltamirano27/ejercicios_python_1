# Función calcularTemperaturaMedia: Recibe dos números reales que representan 
# dos temperaturas y devuelve la temperatura media.
#Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def temperatura_media(temp1, temp2):
    return (temp1 + temp2) / 2

if __name__ == "__main__":
    temps = int(input('Cuantas temperaturas vas a calcular? '))
    for i in range(temps):
        temp1 = float(input("Introduce la primera temperatura: "))
        temp2 = float(input("Introduce la segunda temperatura: "))

        print(f'La temperatura media es: {temperatura_media(temp1, temp2)} ')
