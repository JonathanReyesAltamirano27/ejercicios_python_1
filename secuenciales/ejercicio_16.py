# Proceso CalcularAdelantamiento en Python

# Pedir datos al usuario
velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

# Calcular tiempo de alcance (en horas)
tiempo_horas = distancia / (velocidad1 - velocidad2)

# Convertir a minutos
tiempo_minutos = tiempo_horas * 60

# Mostrar resultado
print(f"Lo alcanza en {tiempo_minutos:.2f} minutos.")