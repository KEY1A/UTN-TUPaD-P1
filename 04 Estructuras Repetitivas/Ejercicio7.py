"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numero = int(input("Ingresa un número entero positivo: "))

suma = sum(range(numero + 1))

print(f"La suma de los números entre 0 y {numero} es {suma}.")
