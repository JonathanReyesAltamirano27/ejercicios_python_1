# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana
# Para esto, se registran los dí­as que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
# y además calcule cuánto pagó la empresa por los N empleados.


if __name__ == "__main__":
    print("\n========================================")
    print("       CÁLCULO DE NÓMINA")
    print("========================================\n")
    
    
    trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
    sueldo_por_hora = float(input("Sueldo por hora: "))

    horas_acum = 0

    for trabajador in range(1, trabajadores + 1):
        horas_por_trabajador = 0
        dias = int(input(f"\n¿Cuántos días ha trabajado el trabajador {trabajador}?: "))
        
        
        for dia in range(1, dias + 1):
            horas = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador} el día {dia}?: "))
            horas_por_trabajador += horas
        
        sueldo_trabajador = horas_por_trabajador * sueldo_por_hora
        print(f"El trabajador {trabajador} tiene de sueldo {sueldo_trabajador}")
        
        
        horas_acum += horas_por_trabajador

    print("\n========================================")
    print(f"El pago a los {trabajadores} trabajadores es: {horas_acum * sueldo_por_hora}")
    print("========================================") 