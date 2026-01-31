sueldo = float(input("Dime el sueldo base: "))
venta1 = float(input("Dime precio de la venta 1: "))
venta2 = float(input("Dime precio de la venta2: "))
venta3 = float(input("Dime precio de la venta3: "))

comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1

print(f"Comisión por ventas:", comision)
print(f"Sueldo total:", sueldo + comision)