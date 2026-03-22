notas = []

for i in range(1, 4):
    nota = int(input(f'Inserta la nota del alumno { i }: '))
    notas.append(nota) 

suma = 0
minima = 10
maxims = 0
for nota in notas:
    suma += nota
    if nota < minima:
        minima = nota
    if nota > maxims:
        maxims = nota

print('La nota mínima es: ', minima)
print('La nota máxima es: ', maxims)
print('La nota media es: ',  suma / 5) 
