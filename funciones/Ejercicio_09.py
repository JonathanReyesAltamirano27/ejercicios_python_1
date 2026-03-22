# Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
# salida e intercambia sus valores si el segundo es mayor que el primero.
# Parámetros de entrada y salida: dos números

def intercambiar(mayor, menor):

    if mayor < menor:
        mayor, menor = menor, mayor
    return mayor, menor

if __name__ == "__main__":
    print("--- Ordenador de dos números ---")
    
    num1 = int(input("Introduce el primer número (que debería ser el mayor): "))
    num2 = int(input("Introduce el segundo número (que debería ser el menor): "))
    num1, num2 = intercambiar(num1, num2)
    
    print("\n¡Listo! Así quedaron ordenados:")
    print(f"El número mayor es: {num1}")
    print(f"El número menor es: {num2}") 