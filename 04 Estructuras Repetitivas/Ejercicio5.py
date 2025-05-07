"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numero_secreto = random.randint(0, 9)
intentos = 0

numero_usuario = int(input("Adivina el número entre 0 y 9: "))

while numero_usuario != numero_secreto:
    intentos += 1
    numero_usuario = int(input("Incorrecto, intenta nuevamente: "))

intentos += 1
print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")