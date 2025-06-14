"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número."""

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    cuenta_actual = 1 if (numero % 10) == digito else 0
    return cuenta_actual + contar_digito(numero // 10, digito)

num = int(input("Ingresá un número entero positivo: "))

digito_valido = False
while not digito_valido:
    dig = int(input("Ingresá un dígito (0-9) para buscar: "))
    if 0 <= dig <= 9:
        digito_valido = True
    else:
        print("Error: el dígito debe estar entre 0 y 9. Intentá nuevamente.")

resultado = contar_digito(num, dig)
print(f"El dígito {dig} aparece {resultado} veces en el número {num}.")

