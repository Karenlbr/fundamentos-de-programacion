"""1. preograma que calcule el promedio de las 4 notas
2. leer 3 notas
3. Calcular promedio 
4. crear la condición para saber si aprobó (if)
5. Crear la condición para saber si no aprobó (else)"""

print("Ingrese e3 notas para saber si aprobo o no")
nota1 = float(input("Ingresala nota 1\t"))
nota2 = float(input("Ingresala nota 2\t"))
nota3 = float(input("Ingresala nota 3\t"))
nota4 = float(input("Ingresala nota 4\t"))
promedio = (nota1 + nota2 + nota3 +nota4)/4
if promedio >= 4.5:
    print(f"Usted aprobó con {promedio:.2f} y su promedio es excelente")
elif promedio >= 4.0 and promedio < 4.5:
    print(f"Usted aprobó con {promedio:.2f} y su promedio es sobresaliente")
elif promedio >= 3.0 and promedio < 3.9:
    print(f"Usted aprobó con {promedio:.2f} y su promedio es aceptable")
elif promedio < 3.0:
    print(f"Usted aprobó con {promedio:.2f} y su promedio es Insufiiciente")

else: 
    print(f"Usted reprobó con {promedio}:.2f")