edades = [] #arreglo vacio
#se creo la variable eda1 para leer
edad1 = int(input("Ingrese las edad 1\t")) 
edades.append(edad1) #se añade la edad 1 al arreglo
edad2 = int(input("Ingrese la edad 2\t")) 
edades.append(edad2) # se añade la edad 2 al arreglo
edad3 = int(input("Ingrese la edad 3\t"))
edades.append(edad3) # se añade la edad 2 al arreglo
edad4 = int(input("Ingrese la edad 4\t")) 
edades.append(edad4) # se añade la edad 2 al arreglo
edad5 = int(input("Ingrese la edad 5\t"))
edades.append(edad5) # se añade la edad 2 al arreglo
promedio = (edades[0] + edades[1] + edades[2] + edades[3] + edades[4])/5
print(f"El promedio de las edades es {promedio}")
