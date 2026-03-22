# Queremos guardar los nombres y la edades de los alumnos de un curso. 
#Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrará los siguientes datos:
# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

if __name__ == "__main__":
    nombres = []
    edades = []
    
    print("--- Registro de Jugadores/Alumnos ---")
    print("(Escribe un asterisco '*' en el nombre para terminar el registro)\n")
    
    while len(nombres) < 30:
        nombre_ingresado = input("Dime el nombre de un alumno: ")
        
        if nombre_ingresado == "*":
            break
            
        edad_ingresada = int(input("Dime su edad: "))
        nombres.append(nombre_ingresado)
        edades.append(edad_ingresada)
        print("-" * 20) 

    if len(edades) > 0:
        edad_max = max(edades)
        
        print("\n=======================")
        print("Alumnos mayores de edad (18+)")
        print("=======================")

        for i in range(len(nombres)):
            if edades[i] >= 18:
                print(nombres[i])
                
        print("\n===============")
        print(f"Alumnos mayores (La edad máxima fue {edad_max})")
        print("===============")
        for i in range(len(nombres)):
            if edades[i] == edad_max:
                print(nombres[i])
                
    else:
        print("\nNo se registraron alumnos.")