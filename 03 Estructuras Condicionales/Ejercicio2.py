"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

nota = int(input("Por favor, escriba su nota: "))

if nota >= 6:
  print("Usted esta aprobado.")
else:
  print("Usted esta desaprobado.")