# Una empresa tiene el registro de las horas que trabaja diariamente un empleado 
# durante la semana (seis días) y requiere determinar el total de éstas, así como 
# el sueldo que recibirá por las horas trabajadas.

if __name__ == "__main__":
    print("--- Calculadora de Sueldo Semanal ---")
    
    sueldo_por_hora = float(input("Introduce el sueldo por hora: $"))
    
    
    horas_acum = 0
    

    for dia in range(1, 7):
        horas = int(input(f"¿Cuántas horas has trabajado el día {dia}?: "))
        
        
        horas_acum += horas
        
    
    print("\n--- Reporte de Pago ---")
    print(f"Horas acumuladas en la semana: {horas_acum} horas")
    
    sueldo_total = sueldo_por_hora * horas_acum
    print(f"Sueldo total a recibir: ${sueldo_total}") 