def coste_transporte():
    # Solicitar el peso del paquete
    peso = int(input("¿Qué peso tiene el paquete (en gramos)?: "))
    
    # Validar el peso (máximo 5000 gramos = 5 kg)
    if peso > 0 and peso <= 5000:
        print("1.- América del Norte")
        print("2.- América Central")
        print("3.- América del Sur")
        print("4.- Europa")
        print("5.- Asia")
        
        zona = int(input("A qué zona se reparte (1-5): "))
        
        # Calcular coste según la zona
        if zona == 1:
            coste = peso * 24 / 100  # Convertir céntimos a euros
            print(f"Coste: {coste:.2f} euros.")
        elif zona == 2:
            coste = peso * 20 / 100  # Convertir céntimos a euros
            print(f"Coste: {coste:.2f} euros.")
        elif zona == 3:
            coste = peso * 21 / 100  # Convertir céntimos a euros
            print(f"Coste: {coste:.2f} euros.")
        elif zona == 4:
            coste = peso * 10 / 100  # Convertir céntimos a euros
            print(f"Coste: {coste:.2f} euros.")
        elif zona == 5:
            coste = peso * 18 / 100  # Convertir céntimos a euros
            print(f"Coste: {coste:.2f} euros.")
        else:
            print("Zona incorrecta.")
    else:
        print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")

# Llamar a la función
coste_transporte()