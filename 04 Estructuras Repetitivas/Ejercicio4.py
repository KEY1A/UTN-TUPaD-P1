"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuenia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

total = 0
num = int(input("Ingresa un número entero (0 para finalizar): "))

while num != 0:
    total += num
    num = int(input("Ingresa un número entero (0 para finalizar): "))

print(f"La suma total de los números ingresados es {total}.")