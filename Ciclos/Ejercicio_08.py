# Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#  A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:
#	* La suma de los números que están dentro del intervalo (intervalo abierto).
#	* Cuantos números están fuera del intervalo.
#	* He informa si hemos introducido algún número igual a los límites del intervalo.

if __name__ == "__main__":
    print("--- Analizador de Intervalos ---")
    
    
    suma_dentro = 0
    cont_fuera = 0
    igual_limites = False  
    

    while True:
        lim_inf = int(input("Introduce el límite inferior del intervalo: "))
        lim_sup = int(input("Introduce el límite superior del intervalo: "))
        
        if lim_inf <= lim_sup:
            break  
        else:
            print("ERROR: El límite inferior debe ser menor que el superior.\n")


    num = int(input("\nIntroduce un número (0, para salir): "))
    
    while num != 0:
        
        
        if lim_inf < num < lim_sup:
            suma_dentro = suma_dentro + num
        else:
            cont_fuera = cont_fuera + 1
            
        if num == lim_inf or num == lim_sup:
            igual_limites = True  
            
    
        num = int(input("Introduce un número (0, para salir): "))

    
    print("\n--- Resultados Finales ---")
    print(f"La suma de los números dentro del intervalo es: {suma_dentro}")
    print(f"La cantidad de números fuera del intervalo es: {cont_fuera}")
    

    if igual_limites:
        print("Se ha introducido algún número igual a los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.") 