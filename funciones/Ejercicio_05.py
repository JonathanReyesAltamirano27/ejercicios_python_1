# Procedimiento CalcularMaxMin: recibe un vector de enteros, su tamaño, y devuelve
#  el máximo y el mínimo de los números guardados en el vector.
#Parámetros de entrada: vector de enteros y tamaño
# Parámetros de entrada y salida: valor máximo y mínimo 

def calcular_max_min(vector):

    maximo = vector[0]
    minimo = vector[0]
    
    for numero in vector:
        if numero > maximo:
            maximo = numero
            
        if numero < minimo:
            minimo = numero
    return maximo, minimo

if __name__ == "__main__":
    puntajes = [45, 12, 89, 34, 8, 56]
    puntaje_alto, puntaje_bajo = calcular_max_min(puntajes)
    
    print(f"La mejor partida fue de: {puntaje_alto} puntos")
    print(f"La peor partida fue de: {puntaje_bajo} puntos") 

