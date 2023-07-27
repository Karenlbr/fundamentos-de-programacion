"""
pseudocodigo
1. crear la variable contador
2. crear el ciclo contador
3. Dentro del ciclo while disminuir el contador
"""

contador = int(input("Ingresar el numero\t"))
while contador > 0:
    if contador >= 1:
        print(contador, end=",  ")
    contador = contador -1
