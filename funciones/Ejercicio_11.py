# Función EsBisiesto: Recibe un año y devuelve si es o no bisiesto
#Parámetros de entrada: año
# Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)

def es_bisiesto(year):
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    print("--- Detector de Años Bisiestos ---")
    
    ano_usuario = int(input("Introduce el año que quieres revisar: "))
    resultado = es_bisiesto(ano_usuario)
    
    if resultado == True:
        print(f"¡El año {ano_usuario} SÍ es bisiesto! Febrero tiene 29 días.")
    else:
        print(f"El año {ano_usuario} NO es bisiesto. Febrero solo tiene 28 días.")