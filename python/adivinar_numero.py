""" 
1. Inportar la libreria random
2. Leer el rango del numero aleatorio
3. Generar el numero aleatorio
4. Crear el ciclo para pedir números al usuario
5. validar si el nuemro que indico el sistema el usuario es el número aleatorio seleccionado
"""
#importar el modulo random
import random as rn
#Leer el rango deñ nuemro aleatorio
print("Ingresa el rango en que se generará el número aleatorio")
inicio =int(input("Inicio = "))
fin = int(input("Fin = "))

#generar el número aleatorio en el rango indicado
numero_aleatorio = rn.randint(inicio, fin)

#pedir numero al usuario
numero_usuario = -1
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Ingresa un numero\t"))
print("¡Felicitaciones!  Encontraste el número")