"""- Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
"""
cantidad = 100
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / cantidad
print(f"La media de los números ingresados es {media:.2f}")