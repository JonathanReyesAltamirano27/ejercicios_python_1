# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
# euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total 
# de lo que pagó después de los 20 meses.

if __name__ == "__main__":
    print("--- Calculadora de Préstamo (Crecimiento Exponencial) ---")
    
    pago_acum = 0.0
    pago = 10.0
    
    
    for mes in range(1, 21):
        
        pago_acum += pago
        
        pago *= 2
        
    print(f"\nAl final de los 20 meses tuvo que pagar en total: ${pago_acum}") 