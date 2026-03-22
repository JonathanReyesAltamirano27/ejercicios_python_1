# Escribe un programa que dados dos números, uno real (base) y un entero positivo 
# (exponente), saque por pantalla el resultado de la potencia. No se puede 
# utilizar el operador de potencia.

if __name__ == "__main__":
    print("--- Calculadora de Potencias ---")
    
    
    base = float(input("Dame la base de la potencia: "))
    
    
    while True:
        exponente = int(input("Dame el exponente de la potencia: "))
        
        if exponente >= 0:
            break  
        else:
            print("ERROR: El exponente debe ser positivo\n")
            
    potencia = 1
    
    
    for i in range(exponente):
        potencia = potencia * base
        
    print(f"\nPotencia: {potencia}") 