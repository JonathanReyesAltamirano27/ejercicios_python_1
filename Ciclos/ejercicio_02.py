# Programa que esconde un número entre 1 y 100

import random

hidden = random.randint(1, 100)

intentos = 1 

while intentos <= 10:
        num = int(input('Adivina el numero: '))
        if num  == hidden:
                 print('Adivinaste!')
                 print('En' ,  'intentos')
                 break
        elif num < hidden:      
                print('uno mayor')
        else:
                print('uno menor')
        intentos += 1

if intentos > 10:
       print('Fallaste XD!')
       print('El número era:' ,hidden) 
