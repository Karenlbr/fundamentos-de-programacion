Algoritmo cesantias_intereses_de_cesantias
	Escribir 'Vamos a hallar el valor de las cesantias y el interes de las cesantias de un trabajador'
	Escribir 'Dame el valor del salario'
	Leer salario
	Escribir "Dame los dias laborados"
	Leer dias
	// Se colocan lo dias laborados y si es año completo es 360
	Escribir "El valor de las cesantias son = " , (salario * dias)/360
	Escribir "El valor del interes de la cesantia = " , ((salario * dias / 360) * (12/100))
FinAlgoritmo
