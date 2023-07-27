"""calcular la suma de los números si el número 1 es mayor que el número 2
pseudocodigo
1. crear las variables la leer los números
2. crear la condicion 

. agregar la suma cuando se cumple la condicion
"""

print("vamos a sumar dos números si el primero es mayor que el segundo")
numero1 = int(input("Ingrese el numero 1\n"))
numero2 = int(input("Ingrese el numero 2\n"))
if numero1 > numero2:
    print(f"la suma de {numero1} + {numero2} es igual a {numero1 + numero2}")
else:
    print("No se puede ejecutar la suma porque no cumple la condición")