import random
numeros = []

for i in range(10):
    numeros.append(random.randint(1, 10))

for n in numeros:
    print(n, 'Su cuadrado: ', n ** 2, 'Su cubo', n **3)