# Proceso CalcularDinero en Python

# Leer cantidad de monedas de cada tipo
euro2 = int(input("Monedas de 2 euros: "))
euro1 = int(input("Monedas de 1 euro: "))
cent50 = int(input("Monedas de 50 céntimos: "))
cent20 = int(input("Monedas de 20 céntimos: "))
cent10 = int(input("Monedas de 10 céntimos: "))

# Calcular euros (monedas de 2€ * 2 + monedas de 1€)
total_euros = euro2 * 2 + euro1

# Calcular céntimos
total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

# Convertir céntimos a euros (división entera entre 100)
total_euros = total_euros + (total_centimos // 100)  # // es equivalente a trunc()
total_centimos = total_centimos % 100

# Mostrar resultado
print(f"{total_euros} euros y {total_centimos} céntimos.")