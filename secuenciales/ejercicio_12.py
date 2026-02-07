import math

def calcular_distancia_entre_puntos():
    # Solicitar coordenadas del primer punto
    x1 = float(input("Dime la coordenada x del punto 1: "))
    y1 = float(input("Dime la coordenada y del punto 1: "))
    
    # Solicitar coordenadas del segundo punto
    x2 = float(input("Dime la coordenada x del punto 2: "))
    y2 = float(input("Dime la coordenada y del punto 2: "))
    
    # Calcular distancia usando la fórmula de distancia euclidiana
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Mostrar resultado
    print(f"Distancia: {distancia}")

# Llamar a la función
calcular_distancia_entre_puntos()