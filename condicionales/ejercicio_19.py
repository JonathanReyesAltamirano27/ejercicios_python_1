def dias_del_mes():
    # Solicitar el número del mes
    mes = int(input("Introduce el número de mes (1-12): "))
    
    # Determinar los días del mes usando match-case (Python 3.10+)
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print("31 días")
        case 2:
            print("28 o 29 días")
        case 4 | 6 | 9 | 11:
            print("30 días")
        case _:
            print("Mes incorrecto")

# Llamar a la función
dias_del_mes()