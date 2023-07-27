"""pseudocodigo
1. leer el numero
2. crear la condicion para saber si es positivo
3. crear la condicion para saber si es negativotivo
3. crear la condicion para saber si es cero
"""
print("Ingrese un numero para saber si es positivo, negativo o cero")
numero = int(input())
if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0:
    print(f"El numero {numero} es negativo")
else:
    print(f"El numero {numero} es cero")
