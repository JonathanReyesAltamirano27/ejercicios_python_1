def calcular_coste_autobus():
    # Solicitar el número de alumnos
    num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))
    
    # Validar que el número de alumnos sea positivo
    if num_alumnos > 0:
        # Determinar el coste por alumno según la cantidad
        if num_alumnos >= 100:
            coste_por_alumno = 65
        elif num_alumnos >= 50:  # Ya sabemos que num_alumnos <= 99 por el elif anterior
            coste_por_alumno = 70
        elif num_alumnos >= 30:  # Ya sabemos que num_alumnos <= 49 por el elif anterior
            coste_por_alumno = 95
        else:  # num_alumnos < 30
            coste_por_alumno = 4000 / num_alumnos
        
        # Calcular el coste total del autobús
        coste_autobus = num_alumnos * coste_por_alumno
        
        # Mostrar resultados
        print(f"El coste por alumno es {coste_por_alumno:.2f} euros.")
        print(f"El coste del autobús es {coste_autobus:.2f} euros.")
    else:
        print("El número de alumnos debe ser un valor positivo.")

# Llamar a la función
calcular_coste_autobus()