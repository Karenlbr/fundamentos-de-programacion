"""pedir al usuario que introduzca un número y determinar si es par o impar  
pseudocodigo
1. Leer el número
2. crear la concion de si el número es par 
3. crear la condición de si el npumero es imapar """

numero = int(input("Ingresa el número para determinar si es par o impar\t5"))
if numero % 2 == 0:
    print(f"El número {numero}es par")
else:
    print(f"El número {numero} es impar")
    