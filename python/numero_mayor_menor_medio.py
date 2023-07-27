"""
Cree un programa para leer tres números enteros y encontrar el mayor, 
el menor y el del medio.

Pseudocódigo
1. Leer el número 1 
2. Leer el número 2
3. Leer el número 3
4. Crear la condición para cada caso (6 casos)
"""
numero1 = int(input("Ingrese el número 1\t"))
numero2 = int(input("Ingrese el número 2\t"))
numero3 = int(input("Ingrese el número 3\t"))
if numero3 > numero2 and numero2 > numero1 and numero3 > numero1:
    print(f"El mayor es {numero3}, el del medio es {numero2} y el menor es {numero1}")
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(f"El mayor es {numero2}, el del medio es {numero3} y el menor es {numero1}")
elif numero3 > numero2 and numero3 > numero1 and numero1 > numero2:
    print(f"El mayor es {numero3}, el del medio es {numero1} y el menor es {numero2}")
elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print(f"El mayor es {numero2}, el del medio es {numero1} y el menor es {numero3}")
elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
    print(f"El mayor es {numero1}, el del medio es {numero3} y el menor es {numero2}")
elif numero1 > numero2 and numero2 > numero3 and numero1 > numero3:
    print(f"El mayor es {numero1}, el del medio es {numero2} y el menor es {numero3}")
else: 
    print(f"Los números son iguales")