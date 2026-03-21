dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = ['Enero', 'Febrero', 'Marzo',
          'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre',
            'Noviembre', 'Diciembre']

mes = int(input('Ingresa un número[1, 12]: '))
print(dias[mes - 1])
print(meses[mes -1])
          