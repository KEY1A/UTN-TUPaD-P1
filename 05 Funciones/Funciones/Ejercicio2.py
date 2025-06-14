"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario."""

def saludo(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(saludo(nombre_usuario))

