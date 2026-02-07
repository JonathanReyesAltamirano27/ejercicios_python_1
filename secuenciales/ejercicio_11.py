def calcular_distancia():
    # Solicitar dos números
    num1 = int(input("Dime el número1: "))
    num2 = int(input("Dime el número2: "))
    
    # Calcular la distancia (valor absoluto de la diferencia)
    distancia = abs(num1 - num2)
    
    # Mostrar el resultado
    print(f"Distancia: {distancia}")

# Llamar a la función
calcular_distancia()