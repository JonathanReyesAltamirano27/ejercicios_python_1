# Función CalcularFactorial: Recibe un número si el número=1 devuelve que el 
# factorial es 1, sino acumula el producto del número con el cálculo del factorial 
# del numero-1. Es una función recursiva.
# Parámetros de entrada: número
# Dato devuelto: Factorial del número

def calcular_factorial(num):
    if num == 1 or num == 0: 
        return 1
    else:
        return num * calcular_factorial(num - 1)

if __name__ == "__main__":
    print("--- Calculadora de Factoriales ---")
    
    numero_usuario = int(input("Introduce un número entero: "))
    resultado = calcular_factorial(numero_usuario)
    
    print(f"El factorial de {numero_usuario} es: {resultado}") 