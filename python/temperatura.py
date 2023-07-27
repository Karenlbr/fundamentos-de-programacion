""" 
1. Crear una calculadora que convierta Grados Centigrados a Grados Kelvin y Grados Farenheit 
2. Igresa los Grados  Centigrados
3. cree la condición de eleccios si el usuario quiere Grados Kelvin
4. Cree la condición de eleccios si el usuario quiere Grados Farenheit
5. cree la condición de error al dar otra respuesta 
6. Ingresa los Grados Centigrados
 """


centigrados = 30
print("Digame si quiere K o F")
respuesta = input()
if respuesta == "K" or respuesta == "k":
    print("Grados Kelvin")
if respuesta == "F" or respuesta == "f":
    print("Grados Farenheit")
if respuesta != "K" and respuesta != "F":
    print("No entiendo su respuesta):")
print("Ingresa el valor de Grados Centigrados")
centigrados = float(input())
kelvin = float(centigrados + 273.15)
farenheit = float((centigrados * (9/5)) + 32)
if respuesta == "K" or respuesta == "k":
    print("El valor en grados Kelvis es"  , + kelvin)
if respuesta == "F"or respuesta == "m":
    print("El valor en grados Farenheit es"  , + farenheit)
