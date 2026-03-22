# Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y 
# devuelve si la fecha es correcta o no.
# Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes
# Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto
# la fecha va a ser incorrecta.
# Parámetros de entrada: día, mes y año
# Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)


def dias_del_mes(month, year):

    if month == 2:
        return 28

    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def validar_fecha(day, month, year):
    if day < 1 or day > dias_del_mes(month, year):
        return False
    else:
        return True

if __name__ == "__main__":
    print("--- Validador de Fechas ---")
    
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes (1-12): "))
    anio = int(input("Introduce el año: "))
    fecha_correcta = validar_fecha(dia, mes, anio)
    
    if fecha_correcta == True:
        print("\n¡Todo en orden! Es una fecha válida del calendario.")
    else:
        print("\n¡Error! Esa fecha no existe. Revisa el día o el mes.") 