"""crear la lista 1
leer 5 nukemros para lista 1
guardar los 5 numeros en la lista 1
crear la lista 2
leer 5 nukemros para lista 2
guardar los 5 numeros en la lista 2
crae lista 3
Extraer los elementos de la lista 2 para calcular el producto ya guardarlo en la lista 3
mostrar la lista 3"""

print("numero para la lista 1")
numero1 = int(input("Ingrese el numero 1\t"))
numero2 = int(input("Ingrese el numero 2\t"))
numero3 = int(input("Ingrese el numero 3\t"))
numero4 = int(input("Ingrese el numero 4\t"))
numero5 = int(input("Ingrese el numero 5\t"))
lista1 = [numero1, numero2, numero3, numero4, numero5] # Guardar los valores en la lista 1

print("numero para la lista 2")
numero1 = int(input("Ingrese el numero 1\t"))
numero2 = int(input("Ingrese el numero 2\t"))
numero3 = int(input("Ingrese el numero 3\t"))
numero4 = int(input("Ingrese el numero 4\t"))
numero5 = int(input("Ingrese el numero 5\t"))
lista2 = [numero1, numero2, numero3, numero4, numero5] #Guardar los valores de la lista 2

lista3 =[]
lista3.append(lista1[0]*lista2[0])
lista3.append(lista1[1]*lista2[1])
lista3.append(lista1[2]*lista2[2])
lista3.append(lista1[3]*lista2[3])
lista3.append(lista1[4]*lista2[4])

print(f"lista 1 {lista1}\nlista 2 {lista2}\nlista 3 {lista3}")