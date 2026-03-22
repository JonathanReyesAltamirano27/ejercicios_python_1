# Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#salida e intercambia sus valores si el segundo es mayor que el primero.
# Parámetros de entrada y salida: dos números

def intercambiar(mayor, menor):

    if mayor < menor:
        mayor, menor = menor, mayor
        
    return mayor, menor

if __name__ == "__main__":
    print("--- Ordenador de Números ---")

 
    num1 = int(input("Introduce el primer número (el que tú quieras): "))
    num2 = int(input("Introduce el segundo número: "))
    
    print(f"\nAntes de la función tus números eran: Primero = {num1}, Segundo = {num2}")
    
    num1, num2 = intercambiar(num1, num2)
    
    print("\n¡Listo! Así quedaron ordenados:")
    print(f"El número mayor es: {num1}")
    print(f"El número menor es: {num2}")