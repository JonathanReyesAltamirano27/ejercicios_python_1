# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
# y, además, calcule cuánto pagó la empresa por los N empleados.

if __name__ == "__main__":
    print("--- Sistema de Nómina Semanal ---")
    
    horas_acum = 0
    
    trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
    sueldo_por_hora = float(input("Sueldo por hora: $"))
    

    for trabajador in range(1, trabajadores + 1):
        
        horas_por_semana = int(input(f"\n¿Cuántas horas ha trabajado el trabajador {trabajador}?: "))

        horas_acum += horas_por_semana
        
        sueldo_individual = horas_por_semana * sueldo_por_hora
        print(f"El trabajador {trabajador} tiene de sueldo: ${sueldo_individual}")
        
    print("\n========================================")
    pago_total = horas_acum * sueldo_por_hora
    print(f"El pago total a los {trabajadores} trabajadores es: ${pago_total}") 