# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales

def convertir_a_segundos(h, m, s):

    segundos_totales = (h * 3600) + (m * 60) + s
    
    return segundos_totales

if __name__ == "__main__":
    print("--- Convertidor de Tiempo a Segundos ---")
    
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    resultado = convertir_a_segundos(horas, minutos, segundos)
    
    print(f"\nEl tiempo total es de: {resultado} segundos.") 