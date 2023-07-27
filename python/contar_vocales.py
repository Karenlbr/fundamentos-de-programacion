"""
cree un programa que cuente el número de vocales en una cadena dada 

pseudocodigo
1. Ingresar la cadena de palabras 
2. Crear la condicion que cuente las vocales 
"""

cadena = input("Ingresa la cadena de palabras:\n")

cadena = cadena.upper()

contador = 0  

for vocal in cadena:
    if vocal in "A,E,I,O,U,a,e,i,o,u": 
        contador += 1

cantidad_vocales = contador
print(f"En la cadena '{cadena}' hay {cantidad_vocales} vocales\n")