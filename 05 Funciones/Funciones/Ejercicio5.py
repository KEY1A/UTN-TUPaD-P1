"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""\

def segundos_a_horas(segundos):
    return segundos / 3600

segundos_del_usuario = float(input("Por favor, ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos_del_usuario)

print(f"{int(segundos_del_usuario)} segundos equivalen a {horas:.2f} horas.")


