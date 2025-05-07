"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""


primer_num = int(input("Ingresa el primer número: "))
segundo_num = int(input("Ingresa el segundo número: "))

suma = sum(range(primer_num + 1, segundo_num))

print(f"La suma de los números entre {primer_num} y {segundo_num}, excluyéndolos, es {suma}.")

