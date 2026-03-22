...
# Funciones en Python
...

#print('un texto') - > imprimir en terminal
#int() - > regresa el valor como entero
#input() - > regresa el texto del teclado
#len() - > regresa el tamaño del objetivo
#range() - > re
...

#Podemos crear funciones
#Definir la función
#def numbre_funciones(parametros):
    #intrucciones
    #return algo

#llamar o ejecutar
#nombre_funcion()
...

# Sin parametros y sin retorno
def hello():
    print('Hola!')

hello() 
hello()
hello()

# Con parametros y sin retorno
def hello_2(name):
    print('Hola', name)
hello_2('Joni')
hello_2('Joss')
hello_2('Jorge')

# Funciones con parametro y con retornos
def duplica(num):
    return num * 2

doble = duplica(15)
print('El doble de 15 es#', doble)

def suma(num1, num2):
    return num1 + num2

result = suma(16, -26)
print(result)

def fullname(name, ap_pat, ap_mat):
    return f"{name} { ap_pat} { ap_mat }"

print(fullname("Jonathan", "Reyes", "Altamirano"))
print(fullname("Reyes", "Altamirano", "Jonathan"))

# Parmetros psosisonales 
print(fullname(ap_pat="Reyes",
               ap_mat="Altamirano",
               name="Jonathan"))

# Parametros opcionales 
def get_hero(name, hero ='Superman'):
    return f"{ name } is { hero }"

print(get_hero("Joni"))
print(get_hero("Emmanuel"))
print(get_hero("Piter Parker", "Spiderman")) 
