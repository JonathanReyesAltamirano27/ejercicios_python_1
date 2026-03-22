
cont_negativos = 0
cont_positivos = 0
cont_ceros = 0

cantidad_num = int(input("¿Cuántos números vas a introducir?: "))

for i in range(1, cantidad_num + 1):
    print(f"Número {i}:", end=" ")
    num = int(input())
    
    if num > 0:
        cont_positivos += 1
    elif num < 0:
        cont_negativos += 1
    else:
        cont_ceros += 1

print(f"Números positivos: {cont_positivos}")
print(f"Números negativos: {cont_negativos}")
print(f"Números igual a 0: {cont_ceros}")