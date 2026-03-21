# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta 
# que seleccionamos la opción de "Salir".

import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    opcion = 0
    while opcion != 5:
        limpiar_pantalla()
        print("\n========================================")
        print("       Menú de recomendaciones")
        print("========================================")
        print("   1. Literatura")
        print("   2. Cine")
        print("   3. Música")
        print("   4. Videojuegos")
        print("   5. Salir")
        print("========================================")
        
        entrada = input("Elija una opción (1-5): ")
        if entrada.isdigit():
            opcion = int(entrada)
        else:
            opcion = 0
        
        print() 
        
        if opcion == 1:
            print("Lecturas recomendables:")
            print(" + Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
            print(" + El juego de Ender (Orson Scott Card)")
            print(" + El sueño de los héroes (Adolfo Bioy Casares)")
        elif opcion == 2:
            print("Películas recomendables:")
            print(" + Matrix (1999)")
            print(" + El último samuray (2003)")
            print(" + Cars (2006)")
        elif opcion == 3:
            print("Discos recomendables:")
            print(" + Despedazado por mil partes (La Renga, 1996)")
            print(" + Búfalo (La Mississippi, 2008)")
            print(" + Gaia (Mägo de Oz, 2003)")
        elif opcion == 4:
            print("Videojuegos clásicos recomendables")
            print(" + Día del tentáculo (LucasArts, 1993)")
            print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
            print(" + Death Rally (Remedy/Apogee, 1996)")
        elif opcion == 5:
            print("Gracias, vuelva prontos")
        else:
            print("Opción no válida")
        
        if opcion != 5:
            input("\nPresione Enter para continuar...") 