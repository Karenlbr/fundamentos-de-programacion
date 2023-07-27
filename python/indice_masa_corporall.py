""" pseudocodigo calcular el IMC indicado al usuario su estado de salud
1. leer peso del usuario
2. Leer la estatura del ususario
3. crear la condicion para saber si tiene peso bajo
4. crear la condicion para saber si tiene peso normal 
5. crear la condicion para saber si tiene peso sobrepeso
6. crear la condicion para saber si tiene peso de obesidad I
7. crear la condicion para saber si tiene peso de obesidad II
8. crear la condicion para saber si tiene peso obesidad III 
9. crear la condicion para saber si tiene peso obesidad IV
"""
print("Hallar el indice de masa corporal de una persona")
print("Escribe el peso")
peso = int(input())
print("Escribe la estatura")
estatura = float(input())
imc = float(peso/(estatura*estatura))
print("El indice de masa corporal es" , + imc)
if (imc < 18.5):
    print("Usted tiene bajo peso")
if imc >= 18.5 and imc <= 24.9:
    print("Usted tiene un peso normal")
if imc >= 25 and imc <=29.9:
    print("Usted tiene sobrepeso")
if imc >= 30 and imc <=34.9:
    print("Usted tiene Obesidad I")
if imc >= 35 and imc <=39.9:
    print("Usted tiene Obesidad II")
if imc >= 40 and imc <=49.9:
    print("Usted tiene Obesidad III")
if imc > 50: 
    print("Usted tiene Obesidad III")
    