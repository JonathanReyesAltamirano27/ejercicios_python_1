# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import os
import time

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    print("\n========================================")
    print("         CRONÓMETRO")
    print("========================================\n")
    
    for hora in range(24):
        for minuto in range(60):
            for segundo in range(60):
                limpiar_pantalla()
                print("\n========================================")
                print(f"         {hora:02d}:{minuto:02d}:{segundo:02d}")
                print("========================================\n")
                time.sleep(1) 