import math

def calcular_raices():
    # Solicitar el número
    num = float(input("Dime el número: "))
    
    # Calcular raíz cuadrada
    raiz_cuadrada = math.sqrt(num)
    
    # Calcular raíz cúbica
    raiz_cubica = num ** (1/3)
    
    # Mostrar resultados
    print(f"Raíz cuadrada: {raiz_cuadrada}")
    print(f"Raíz cúbica: {raiz_cubica}")

# Llamar a la función
calcular_raices()