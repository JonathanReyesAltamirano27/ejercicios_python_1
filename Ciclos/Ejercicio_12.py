# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; 
# además, se quiere saber cuánto lleva ahorrado cada mes.

if __name__ == "__main__":
    print("--- Calculadora de Ahorro Anual ---")
    
    
    ahorro_acum = 0.0  
    
    for mes in range(1, 13):
        
        cant_mensual = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: $"))
        
        ahorro_acum = ahorro_acum + cant_mensual
        
        print(f"-> En el mes {mes} llevas ahorrado un total de: ${ahorro_acum}\n")
        
    print("========================================")
    print(f"¡Año terminado! Tu ahorro total fue de: ${ahorro_acum}") 