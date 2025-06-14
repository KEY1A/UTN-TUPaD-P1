"""Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto"""

def decimal_a_binario(n):
    if n == 0:
        return ""  
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
num = int(input("Ingrese un número entero positivo: "))

if num < 0:
    print("Por favor, ingrese un número positivo.")
elif num == 0:
    print("El número binario es 0")
else:
    resultado = decimal_a_binario(num)
    print(f"El número {num} en binario es: {resultado}")