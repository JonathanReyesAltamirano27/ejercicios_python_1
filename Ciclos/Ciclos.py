# Range(5) # 0, 1, 2, 3, 4,
print("Range con un parametro")
for i in range(5):
    print(i)

print()
print("Range con dos parametros")

# Range(2, 5) [2, 3, 4]
for i in range(2, 5):
    print(i)

print()
print("Range con tres parametros")
# range(1, 10, 2) [1, 3, 5, 7, 9]
for i in range(1, 10, 2):
    print(i)

message = "Los dormidos puntos menos"
for letra in message:
    print(letra, end=" - ")
print()  # Agregar nueva línea al final

# Ejemplo de while con condición booleana
exp_bool = True
contador = 1
while exp_bool:
    print(contador)
    contador += 1
    if contador > 5:
        exp_bool = False

# Ejemplo de while con condición numérica
i = 1
while i <= 5:
    print(i)
    i += 1

# Ejemplo de bucle while con input
message = input('Escribe Salir para salir: ')
while message != 'Salir':
    message = input('Escribe Salir para salir: ')

# Otro ejemplo de while True con break
while True:
    message = input('Escribe (S) para salir: ')
    if message == 'S':
        break
