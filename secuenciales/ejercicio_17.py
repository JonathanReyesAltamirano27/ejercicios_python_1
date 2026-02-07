# Proceso CalcularHoraLlegada en Python

# Leer la hora de salida
horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))

# Leer el tiempo de viaje en segundos
segviaje = int(input("Tiempo que has tardado en segundos: "))

# Convertir la hora de salida a segundos desde medianoche
seginicial = horapartida * 3600 + minpartida * 60 + segpartida

# Sumar los segundos de viaje
segfinal = seginicial + segviaje

# Convertir los segundos totales a horas, minutos y segundos
horallegada = segfinal // 3600  # División entera para las horas
minllegada = (segfinal % 3600) // 60  # Resto de segundos convertido a minutos
segllegada = (segfinal % 3600) % 60  # Segundos restantes

# Mostrar la hora de llegada
print("Hora de llegada")
print(f"{horallegada}:{minllegada}:{segllegada}")