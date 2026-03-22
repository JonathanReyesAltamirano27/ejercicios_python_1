# Crear un programa de ordenador para gestionar los resultados de la quiniela de 
# fútbol. Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre 
# de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene 
# dos columnas, en la primera se guarda el número de goles del equipo que está 
# guardado en la primera columna de la tabla anterior, y en la segunda los goles 
# del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el 
# resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

if __name__ == "__main__":
    num_equipos = 3 
    
    equipos = []    
    resultados = [] 
    
    print("--- Registro de Partidos ---")
    for i in range(num_equipos):
        
        eq1 = input(f"\nIntroduce el nombre del equipo 1 del partido {i+1}: ")
        eq2 = input(f"Introduce el nombre del equipo 2 del partido {i+1}: ")
        equipos.append([eq1, eq2])
        
        
        goles1 = int(input(f"Introduce los goles metidos por {eq1}: "))
        goles2 = int(input(f"Introduce los goles metidos por {eq2}: "))
        resultados.append([goles1, goles2])



    print("\nQUINIELA")
    print("========")
    
    for i in range(num_equipos):
        
        equipo_local = equipos[i][0]
        equipo_visitante = equipos[i][1]
        goles_local = resultados[i][0]
        goles_visitante = resultados[i][1]
        
        
        if goles_local > goles_visitante:
            print(f"{equipo_local} - {equipo_visitante} -> 1")
            
        elif goles_local < goles_visitante:
            print(f"{equipo_local} - {equipo_visitante} -> 2")
            
        else:
            print(f"{equipo_local} - {equipo_visitante} -> X") 