def dia_de_la_semana():
    # Solicitar el número del día
    dia = int(input("Dime un día de la semana (1-7): "))
    
    # Determinar el día usando match-case (Python 3.10+)
    match dia:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miércoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sábado")
        case 7:
            print("Domingo")
        case _:
            print("Día incorrecto")

# Llamar a la función
dia_de_la_semana()