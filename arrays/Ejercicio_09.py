# Queremos guardar la temperatura mínima y máxima de 5 días. realiza un programa 
# que de la siguiente información:
# * La temperatura media de cada día
# * Los días con menos temperatura
# * Se lee una temperatura por teclado y se muestran los días cuya temperatura 
# máxima coincide con ella.Si no existe ningún día se muestra un mensaje de 
# información.

if __name__ == "__main__":

    temperaturas = []
    cant_dias = 5
    
    print("--- Registro de Temperaturas ---")
    for i in range(cant_dias):
    
        temp_min = float(input(f"Día {i+1}. Temperatura mínima: "))
        temp_max = float(input(f"Día {i+1}. Temperatura máxima: "))
        
        temperaturas.append([temp_min, temp_max])
        
    print("\nTemperaturas medias")
    print("===================")
    for i in range(cant_dias):
        media = (temperaturas[i][0] + temperaturas[i][1]) / 2
        print(f"Día {i+1}. Temperatura media: {media}")
        
    temp_min_historica = temperaturas[0][0]
    
    for i in range(cant_dias):
        if temperaturas[i][0] < temp_min_historica:
            temp_min_historica = temperaturas[i][0]
            
    print("\nDías con menos temperatura")
    print("==========================")
    for i in range(cant_dias):
        if temperaturas[i][0] == temp_min_historica:
            print(f"Día {i+1}")
            
    print("\nBuscador de temperatura máxima")
    print("===========================")
    temp_buscada = float(input("Introduce una temperatura máxima para buscar: "))
    existe_temperatura = False
    
    for i in range(cant_dias):
        if temperaturas[i][1] == temp_buscada:
            print(f"Día {i+1}")
            existe_temperatura = True
            
    if existe_temperatura == False:
        print("No hay ningún día con dicha temperatura.") 