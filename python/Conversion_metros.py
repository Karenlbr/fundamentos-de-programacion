"""Leer una medida de longitud en metros (m) y presentar su conversión a yardas, pulgadas, pulgadas y centímetros.
Pseudocodigo
1. Ingresar valor
2. Convertir metros en yardas
3. Convertir metros en pulgadas 
4. Convertir metros en pies
5. Convertir metros en centrimetros
 """
metros = float(input("Ingresa el valor en metros \n"))
Yardas = metros * 1.09361
pulgadas = metros * 39.3701
pies = metros * 3.2808
centimetros = metros * 100
print(f"El valor en yardas es {Yardas}\nEl valor en pulgadas es {pulgadas}\nEl valor en pies es {pies}\nEl valor en cntimetros es {centimetros}")