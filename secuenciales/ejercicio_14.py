# Proceso CalcularDecenasUnidades en Python

# Pedir al usuario un número de dos cifras
num = int(input("Dime un número de dos cifras: "))

# Calcular decenas y unidades
decenas = num // 10  # División entera (equivalente a trunc(num/10))
unidades = num % 10   # Módulo (resto de la división)

# Mostrar resultados
print("Primera cifra (decenas):", decenas)
print("Segunda cifra (unidades):", unidades)