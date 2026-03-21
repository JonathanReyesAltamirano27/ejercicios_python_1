# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
# divisible por algún otro número.

if __name__ == "__main__":
    print("--- Detector de Números Primos ---")
    
    es_primo = True
    
    numero_es_primo = int(input("Introduce un número para comprobar si es primo: "))
    
    limite = int(numero_es_primo ** 0.5) + 1
    
    
    for num in range(2, limite):
        
        if numero_es_primo % num == 0:
            es_primo = False 
            break    

    if es_primo and numero_es_primo > 1:
        print("\n¡Es Primo!")
    else:
        print("\nNo es Primo") 