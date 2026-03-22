vector = []
vector_raverse = []

for i in range(5):
    vector.append((input(f'Inserta cadena de texto [( i )]: ')))
for i in range(4, -1, -1):
    vector_raverse.append(vector[i])

print(vector)
print(vector_raverse)