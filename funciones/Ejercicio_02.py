#Función EsMultiplo: Recibe dos número e indica si el primero el múltiplo del 
#segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
#Parámetros de entrada: dos números
#Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo 
#del segundo, Falso en caso contrario.

def es_multiplo(num1, num2):
    return num1 % num2 == 0
    
if __name__ == '__main__':
    numero_1 = int(input('Escribe el primer número: '))
    numero_2 = int(input('Escribe el segundo número: '))

    if es_multiplo(numero_1, numero_2):
        print(f'{numero_1} es múltiplo de {numero_2}')
    else:
        print(f'{numero_1} no es múltiplo de {numero_2}')