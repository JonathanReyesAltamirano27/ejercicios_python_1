
def tipo_triangulo():
    # Solicitar las longitudes de los lados
    ladoA = float(input("Introduce longitud lado A: "))
    ladoB = float(input("Introduce longitud lado B: "))
    ladoC = float(input("Introduce longitud lado C: "))
    
    # Comprobar si es triángulo rectángulo (Pitágoras)
    if (ladoA**2 + ladoB**2 == ladoC**2) or (ladoB**2 + ladoC**2 == ladoA**2) or (ladoC**2 + ladoA**2 == ladoB**2):
        print("Triángulo Rectángulo")
    
    # Comprobar tipo de triángulo por lados
    if (ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA) or (ladoC == ladoA and ladoC != ladoB):
        print("Triángulo Isósceles")
    else:
        if ladoA == ladoB and ladoA == ladoC:
            print("Triángulo Equilátero")
        else:
            print("Triángulo Escaleno")

tipo_triangulo()