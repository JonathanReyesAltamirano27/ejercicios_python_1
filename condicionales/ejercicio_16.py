def calcular_coste_telefono():
    # Solicitar datos de la llamada
    tiempo = int(input("¿Cuánto tiempo es la llamada (en minutos)?: "))
    es_domingo = input("¿Es Domingo? (S/N): ").upper()
    
    turno = ""
    if es_domingo == "N":
        turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ").upper()
    
    # Calcular coste base según duración
    if tiempo < 5:
        coste = tiempo * 100
    elif tiempo < 8:
        coste = (tiempo - 5) * 80 + 500  # 500 = 5*100
    elif tiempo < 10:
        coste = (tiempo - 8) * 70 + 240 + 500  # 240 = 3*80
    else:
        coste = (tiempo - 10) * 50 + 140 + 240 + 500  # 140 = 2*70
    
    # Aplicar impuestos según día y turno
    if es_domingo == "S":
        coste += coste * 0.03  # 3% de impuesto
    elif turno == "M":
        coste += coste * 0.15  # 15% de impuesto por la mañana
    else:
        coste += coste * 0.10  # 10% de impuesto por la tarde
    
    # Mostrar resultado
    print(f"El coste de la llamada: {coste / 100:.2f} euros.")

# Llamar a la función
calcular_coste_telefono()