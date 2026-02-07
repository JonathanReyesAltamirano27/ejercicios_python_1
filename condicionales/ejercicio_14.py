def precio_uva():
    # Solicitar datos iniciales
    precio_inicial = float(input("Introduce el precio inicial por kilos de la UVA (centimos): "))
    kilos = int(input("Introduce cuantos kilos has vendido: "))
    tipo = input("Introduce el tipo de la UVA (A/B): ").upper()
    
    # Validar tipo
    if tipo not in ["A", "B"]:
        print("Tipo incorrecto")
        return
    
    # Solicitar tamaño
    tamano = input("Introduce el tamaño de la UVA (1/2): ")
    
    # Validar tamaño
    if tamano not in ["1", "2"]:
        print("Tamaño incorrecto")
        return
    
    # Ajustar precio según tipo y tamaño
    if tipo == "A":
        if tamano == "1":
            precio_inicial += 20
        else:  # tamano == "2"
            precio_inicial += 30
    else:  # tipo == "B"
        if tamano == "1":
            precio_inicial -= 20
        else:  # tamano == "2"
            precio_inicial -= 30
    
    # Calcular precio final
    precio_final = precio_inicial * kilos
    
    # Mostrar resultado (convertir céntimos a euros)
    print(f"La ganancia es {precio_final / 100:.2f} euros.")

# Llamar a la función
precio_uva()