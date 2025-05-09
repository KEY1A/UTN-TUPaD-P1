"""- Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
- Agregar "jugo" a la lista del tercer cliente usando append.
- Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
- Eliminar "pan" de la lista del primer cliente.
- Imprimir la lista resultante por pantalla
"""

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)