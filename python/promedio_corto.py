#programa que calcula el promedio de 3 notas
nota1 = float(input("Ingresa el valor de la nota de conocimiento(30%)\t"))
nota2 = float(input("Ingresa el valor de la nota de producto (35%)\t"))
nota3 = float(input("Ingresa el valor de la nota (35%)\t"))
promedio = (nota1 * 0.3) + (nota2 * 0.35 + nota3 * 0.35)
print(f"El promedio de las 3 notas es {promedio:.3f} ")
