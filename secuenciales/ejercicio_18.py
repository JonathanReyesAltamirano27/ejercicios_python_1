# Proceso Iniciales en Python

# Leer datos del usuario
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

# Obtener las iniciales
# En Python, [0] obtiene el primer carácter de una cadena (similar a subcadena(nombre,0,0))
inicial = nombre[0] + apellido1[0] + apellido2[0]

# Convertir a mayúsculas
inicial = inicial.upper()

# Mostrar resultado
print(f"Las iniciales son: {inicial}")