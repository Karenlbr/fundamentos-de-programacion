Algoritmo seguridad_social
	// se calcula el equivalente en peso al 8.5% de descuento al trajador y el valor exacto que recibe
	Escribir "Calculo en pesos de aporte a seguridad social"
	Escribir "Dame la cantidad de horas trabajadas"
	Leer horas_semanales
	Escribir "Dame el valor de la hora"
	Leer valor_hora
	Escribir "Dame el valor del porcentaje de la seguridad social"
	Leer porcentaje
	Escribir "el valor equivalente en pesos es = ", (horas_semanales * valor_hora ) *(porcentaje/100)
	Escribir "El valor recibido por el trabajador es de = " , (horas_semanales * valor_hora) - ((horas_semanales * valor_hora)*(porcentaje / 100))
FinAlgoritmo
