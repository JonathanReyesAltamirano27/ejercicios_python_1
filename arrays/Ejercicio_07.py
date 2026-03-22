list_1 = []
list_2 = []
list_3 = []

for i in range(5):
    num = int(input('Ingresa el valor [{ i + 1 }] del vector 1:  '))
    list_1.append(num)
    num = int(input('Ingresa el valor [{ i + 1 }] del vector 2:  '))
    list_2.append(num)

    list_3.append(list_1[i] + list_2[i])

print(list_1)
print(list_2)
print(list_3) 