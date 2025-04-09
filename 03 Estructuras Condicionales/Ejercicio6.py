"""6)Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)] 

print(f"Números aleatorios: {numeros_aleatorios}")


moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")



                      
