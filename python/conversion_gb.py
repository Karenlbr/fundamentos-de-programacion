"""Leer la cantidad de GB (gigabytes)de almacenamiento de un computador y convertirlo a TB (terabytes) y KB (kilobytes).
pseudocodigo
1. Crear la variaable de leer GB
2. Crear variable gigabytes 
3. Crear variable de Kilobytes"""

gigabytes = float(input("Ingresa la cantidad de gigabytes\n"))
terabytes = gigabytes / 1024
kilobytes = gigabytes*(1024*1024)
print(f"La conversion de gigabytes a terabytes es {terabytes}\nla conversion de gigabytes es de {kilobytes}\n")
