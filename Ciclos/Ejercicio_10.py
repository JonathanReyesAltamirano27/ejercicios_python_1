# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

if __name__ == "__main__":
    print("--- Tablas de Multiplicar (del 1 al 5) ---")

    for tabla in range(1, 6):
        print(f"\n--- Tabla del {tabla} ---")
        
        for num in range(1, 11):
            print(f"{tabla} * {num} = {tabla * num}")
    
        input("\nPresiona Enter para ver la siguiente tabla...")
        
    print("\n¡Terminaste todas las tablas!")  