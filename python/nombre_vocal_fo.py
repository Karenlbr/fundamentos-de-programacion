"""psudocodigo
1. Ingresa el nombre
2. crea la variable que empieza por vocal
3. crea la condicion
""" 

vocales = ["A", "E" "I", "O", "U", "a", "e" "i", "o", "u"]
nombre = input("Ingresa tu nombre\t")
empieza_por_vocal = False
for vocal in vocales:
    if nombre[0] == vocal:
        empieza_por_vocal =True
if empieza_por_vocal == True:
    print(f"Elnombre { nombre} empieza por vocal")
else:
    print(f"El nombre {nombre} no empieza por vocal")
