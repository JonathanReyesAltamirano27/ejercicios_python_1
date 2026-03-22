# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
#Además va incrementa el numero de internos que la recibe como parámetro de 
# entrada/salida
# Parámetros de entrada: nombre y contraseña
# Parámetros de entrada y salida: intentos
# Dato devuelto: Valor lógico indicando si ha hecho login

def login(nombre, password, intentos):
    if nombre == "Reyes27" and password == "Jonireyes15":
        return True, intentos
    else:
        intentos = intentos + 1
        return False, intentos

if __name__ == "__main__":
    
    intentos_actuales = 0
    
    print("--- Portal de Acceso VTX E-SPORTS ---")
    
    usuario_ingresado = input("Escribe tu nombre de usuario: ")
    contrasena_ingresada = input("Escribe tu contraseña: ")
    acceso, intentos_actuales = login(usuario_ingresado, contrasena_ingresada, intentos_actuales)
    
    if acceso == True:
        print("\n¡Acceso concedido! Bienvenido al servidor.")
    else:
        print(f"\nAcceso denegado losiento bye  :) ")
