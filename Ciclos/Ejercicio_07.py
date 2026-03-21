# Realizar una algoritmo que muestre la tabla de multiplicar de un número 
# introducido por teclado.

if __name__ == "__main__":
    print("--- Generador de Tablas de Multiplicar ---")
    

    tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))
    
    for num in range(1, 11):
        
        print(f"{num} * {tabla} = {num * tabla}") 