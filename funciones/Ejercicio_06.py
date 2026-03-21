# Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia y
# devuelve el área y el perímetro.
# Parámetros de entrada: radio (real)
# Parámetros de entrada y salida: área y perímetro (real)

import math 

def calcular_area_perimetro(radio):
   
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

if __name__ == "__main__":
    mi_radio = 5
    resultado_area, resultado_perimetro = calcular_area_perimetro(mi_radio)
    
    print(f"Para un radio de {mi_radio}:")
    print(f"El área es: {round(resultado_area, 2)}")
    print(f"El perímetro es: {round(resultado_perimetro, 2)}") 

