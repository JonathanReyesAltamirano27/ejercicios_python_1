# Escribir un programa que imprima todos los números pares entre dos números que 
# se le pidan al usuario.

if __name__ == "__main__":
    print("--- Generador de Números Pares ---")
    
    
    num1 = int(input("Introduce el número 1 (inicio): "))
    num2 = int(input("Introduce el número 2 (límite): "))
    
    if num1 % 2 == 1:
        num1 = num1 + 1  
        
    for num in range(num1, num2 + 1, 2):
        
        print(num, end=" ")
    print() 