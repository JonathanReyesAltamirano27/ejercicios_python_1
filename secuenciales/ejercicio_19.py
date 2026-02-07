# Proceso CalcularPuntos en Python

# Leer cantidad de respuestas correctas e incorrectas
correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))

# Calcular puntos
puntos = correctas * 5 + incorrectas * (-1)

# Mostrar resultado
print(f"Puntos: {puntos}")