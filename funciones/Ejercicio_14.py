# Procedimiento IncializarPila: Recibe un vector (pila) y su tamaño. 
# Recorre el vector e inicializa sus elementos a *. 
# El * representa que el elemento está vacío.
# Parámetros de entrada: Tamaño del vector
# Parámetros de entrada y salida: El vector (pila)

def inicializar_pila(size_pila):
    pila = []  
    
    for i in range(size_pila):
        pila.append(" :) ")  
    return pila

if __name__ == "__main__":
    print("--- Inicializador de Pilas ---")
    
 
    tamano = int(input("¿De qué tamaño quieres crear la pila?: "))
    mi_pila = inicializar_pila(tamano)
    
    print("\n¡Pila inicializada con éxito! Así se ve ahora:")
    print(mi_pila) 