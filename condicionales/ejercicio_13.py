def fecha_correcta():
    # Solicitar día, mes y año
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduce el mes: "))
    year = int(input("Introduce el año: "))
    
    # Inicializar variable para días del mes
    dias_del_mes = 0
    
    # Determinar días del mes según el número de mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_del_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_del_mes = 30
    elif mes == 2:
        # Verificar si es año bisiesto
        if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    else:
        print("Fecha incorrecta: mes inválido")
        return  # Salir de la función
    
    # Verificar si el día está dentro del rango válido
    if dia < 1 or dia > dias_del_mes:
        print("Fecha incorrecta: día inválido")
    else:
        print("Fecha correcta")

# Llamar a la función
fecha_correcta()