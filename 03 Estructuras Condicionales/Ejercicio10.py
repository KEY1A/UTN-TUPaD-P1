"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""


hemisferio = input("Ingrese su hemisferio (N para norte, S para sur): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))


if hemisferio not in ("N", "S"):
    print("Hemisferio no válido. Ingrese 'N' para norte o 'S' para sur.")
else:
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or mes in (10, 11) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    else:
        if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or mes in (10, 11) or (mes == 12 and dia <= 20):
            estacion = "Primavera"


    print(f"Según los datos ingresados, la estación es: {estacion}.")
