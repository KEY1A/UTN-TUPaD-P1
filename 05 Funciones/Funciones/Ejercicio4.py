"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

import math

def obtener_area_circulo(radio):
    return math.pi * radio ** 2

def obtener_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio_del_usuario = float(input("Por favor, ingresa el radio del círculo: "))

area = obtener_area_circulo(radio_del_usuario)
perimetro = obtener_perimetro_circulo(radio_del_usuario)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
