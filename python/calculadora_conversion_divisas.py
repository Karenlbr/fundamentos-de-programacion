""" Crear una calculadora de conversion de divisas. Debe permitir ingreasr pesos colombianos y convertirlos a 5 monedas extranjeras diferentes
pseudocodigo
1. Ingresar valor en peso colombiano
2. Crear variable de Dolares
3. Crear variable de Libra esterlina
4. Crear variable de Reales 
5. Crear variable de yuanes
6. Crear variable de Euros"""

peso_colombiano = float(input("ingresar el valor en peso Colombiano\n"))
dolares = peso_colombiano * 3969
libra_esterlina = peso_colombiano * 5102
reales = peso_colombiano * 830
yuanes = peso_colombiano * 552
Euro = peso_colombiano * 4418
print(f"El valor en Dolares es {dolares}\nEl valor en Libra Esterlina es {libra_esterlina}\nEl valor en Reales es {reales}\nEl valor en yuanes es {yuanes}\nEl valor en Euros es {Euro} ")