# Programa que calcula el factorial de un número
# Con for

# 5 factorial = 1 * 2 * 3 * 4 * 5

num = int(input("Ingresa un número: "))

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * 1 

print('El factorial de', num, 'es', factorial)