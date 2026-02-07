# Proceso CalcularYearBisiesto
year = int(input("Introduce el año: "))

# Regla para años bisiestos:
# Si es divisible por 4 y no divisible por 100, o divisible por 400.
if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
    print("Año bisiesto.")
else:
    print("Año no bisiesto.")