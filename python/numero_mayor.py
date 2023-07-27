""" Pedir al usuario que introduzca dos numeros y determie cual es mayor 
pseudocodigo 
1. Ingresa número 1
2. Ingresa número 2
3. Crear la condición para saber cual es mayor """

numero1 = int(input(f"Ingresa el primer valor \t"))
numero2 = int(input(f"Ingresa el segundo valor\t"))
if numero1 > numero2:
    print(f"El número {numero1} es mayor que el número {numero2}")
else:
    print(f"El número {numero2} es mayor que el numero {numero1}")