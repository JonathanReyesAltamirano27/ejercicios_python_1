# Proceso IntercambiarVariables en Python

# Pedir al usuario los valores de las variables
a = int(input("Introduce valor de la variable A: "))
b = int(input("Introduce valor de la variable B: "))

# Mostrar valores originales (opcional, no estaba en el original)
print(f"Valores originales: A = {a}, B = {b}")

# Intercambiar valores usando variable auxiliar
aux = a
a = b
b = aux

# Mostrar valores intercambiados
print(f"Nuevo valor de A: {a}")
print(f"Nuevo valor de B: {b}")