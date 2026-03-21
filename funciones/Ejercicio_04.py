# Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra 
# con los mismos caracteres separados con espacio.
# Parámetros de entrada: Cadena de caracteres
# Dato devuelto: Cadena igual a la anterior pero con espacios entre los 
# caracteres

def convertir_espaciado(cadena):
    resultado = ""
    
    for letra in cadena:
        resultado = resultado + letra + " "
        
    return resultado

texto_original = "RAYMIX"
texto_modificado = convertir_espaciado(texto_original)

print("Texto original:", texto_original)
print("Texto con espacios:", texto_modificado) 
