# Procedimiento IncializarCola: Recibe un vector (cola) y su tamaño. 
# Recorre el vector e inicializa sus elementos a *. 
# El * representa que el elemento está vacío.
# Parámetros de entrada: Tamaño del vector
# Parámetros de entrada y salida: El vector (cola)

def inicializar_cola(size_cola):
    cola = []  
    
    for i in range(size_cola):
        cola.append("*")  
    return cola

if __name__ == "__main__":
    print("--- Inicializador de Colas ---")
    
    tamano_cola = int(input("¿Cuántos lugares tendrá la cola de espera?: "))
    mi_cola = inicializar_cola(tamano_cola)
    
    print("\n¡Cola inicializada con éxito! Así se ven los espacios:")
    print(mi_cola) 