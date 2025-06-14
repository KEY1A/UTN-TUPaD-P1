"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

num = int(input("Ingrese un número entero: "))

if num < 1:
    print("Por favor, ingrese un número mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {num}:")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")
