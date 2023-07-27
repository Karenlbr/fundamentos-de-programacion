"""pseudocodigo
1. Guardar un numero
2. Ingresa el numero
3. Guardar los nuemro añadidos"""
numeros = []
while True:
    print(f"\033[4;35m"+"\n¡Hola!\n1. Guardar un numero\n2. Ver números guardado"
          "\n0. Salir\n")
    opcion = int(input())
    if opcion == 1:
        numero = int(input("Ingresa el número que deseas añadir\t"))
        numeros.append(numero)
        print(f"El numero {numero} fue guardado de forma exitosa")
    elif opcion == 2:
        print(numeros)
        print(f"Los numeros guardados son {numeros}")
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción válida")
    