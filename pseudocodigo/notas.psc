Algoritmo notas
	Escribir "Vamos a hallar la nota final"
	// Recuerda que el ponderado de conocimiento es del porcentaje de la nota asignada por el docente
	Escribir "Dame la nota de conocimiento (30%)"
	Leer nota_conocimiento
	Escribir "Dame la nota de producto (35%) "
	Leer nota_producto
	Escribir "Dame la nota de desempe�o (35%) "
	Leer nota_desempe�o
	Escribir "La nota final es = " , (nota_conocimiento * (30 / 100)) + (nota_conocimiento * (35 / 100 )) + (nota_desempe�o * (35 / 100 ))
FinAlgoritmo
