""" Este programa pide quue s eingreese un numero , si  el numero es cero el programa se detiene"""
# numero = int(input("Ingrese un numero"))
# if numero != 0:
#     print("Ingrese otro numero")
# else:
#     print("Adiós")


# numero = 1
# while numero != 0:
#     numero = int(input("Ingrese un numero\t"))

# password =0
# contador =0
# while password != 0:
#     password = int(input("Ingrese un contraseña\t"))
#     if contador <= 3:
#         print("Ingrese nuevamente la contraseña")
#     else:
#         print("Lo siento, restablezca su contraseña")

password =0
contador =0
while contador < 3:
    password = int(input("Ingrese un contraseña\t"))
    contador = contador + 1
    if password == 1234:
        print("Su contraseña es correcta, bienvenido")
        contador = 3
    else:
        if contador == 3:
            print("por favor restablesca pla contraseña")
        else:
            print("su contraseña es incorrecta, intente nuevamente")
         