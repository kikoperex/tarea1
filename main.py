# > <					ALGORITMOS DE ENTRADA
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# El programa pregunta con que escala se evaluará a los alumnos, si de 1 a 100, o de 1 a 10
correcto = False
# La variable "correcto" es utilizada confirmar al while q el usuario sí ingresó 1 o 2, si no lo ingresa
# La variable continua en False y el ciclo se repite, si el usuario si lo ingresa se convierte en True
# y el ciclo termina continuando con el programa
evaluaciónEscala = 0
# La variable evaluaciónEscala, por el momento es temporal en lo que se construye la lógica del programa, pero le
# Servirá al programa a hacer los calculos dependiendo si se evalua de 1 a 100, o de 1 a 10
while correcto == False:
	print("Elige una escala para calificar. Puede ser del 1 al 100, o del 1 al 10")
	print("Ingresa 1 para calificar del 1 al 100")
	print("Ingresa 2 para calificar del 1 al 10")
	escala = input()
	if escala == "1":
		evaluaciónEscala = 60
		correcto = True

	elif escala == "2":
		evaluaciónEscala = 6
		correcto = True
	else:
		print("No haz presionado 1 o 2")

# La lógica es simple, un ciclo que pregunta que escala se debe usar, 1 para evaluar de 1 a 100, y 2 para evaluar de
# 1 a 10, si el usuario ingresa mal, se repite el ciclo, si el usuario ingresa bien, se termina y se definen la variables

#-----------------------------------------------------------------------------------------------

correcto = False
# Reutilizo la variable correcto con el mismo próposito, la es definida como False de nuevo, para que ambos whiles utilicen
# La misma lógica

while correcto == False:
	estudiantes = int(input("Cúantos estudiantes quieres evualuar? pueden ser un máximo de 100: ")) # El usuario define cuantos estudiantes evaluará
	if estudiantes >= 1 and estudiantes <= 100:
		correcto = True
	else:
		print("Ingresaste más estudiantes, o un formato invalido")
# La lógica de nuevo es simple, el programa pregunta al usuario ingresar un número máximo de 100
# Si lo hace, se termina el ciclo, sino le hace saber que lo vuelva a ingresar, y se repite el ciclo

#------------------------------------------------------------------------------------------------
correcto = False
# Se vuelve a reutilizar correcto con el mismo proposito que las veces anteriores
while correcto == False:
	calificaciones = input("Ingresa las calificaciones de los estudiantes, separas con un espacio, y tienen que ser enteros: ").split()
	c = 0

	while c < len(calificaciones):
		calificaciones[c] = int(calificaciones[c])
		c = c + 1
	if len(calificaciones) != estudiantes:
		print("La cantidad de calificaciones que haz ingresado no coincide con la cantidad de alumnos que quieres evaluar")
	else:
		correcto = True

# 					FIN DE LOS ALGORITMOS DE ENTRADA
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#						   CALCULOS



promedio = 0
cuentaAprobados = 0
cuentaReprobados = 0
conteoPromedio = 0
sumaCalificaciones = 0
c = 0

while c < len(calificaciones):
	if calificaciones[c] < evaluaciónEscala:
		cuentaReprobados = cuentaReprobados + 1
	elif 6 < calificaciones[c]:
		cuentaAprobados = cuentaAprobados + 1

	while conteoPromedio < len(calificaciones):
		sumaCalificaciones = sumaCalificaciones + calificaciones[conteoPromedio]
		conteoPromedio = conteoPromedio + 1
	promedio = sumaCalificaciones / len(calificaciones)


	c = c + 1
#						FIN DE LOS CALCULOS
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#						   VISUALIZACIÓN


print("									")
print("La calificación promedio de los estudiantes es: ", promedio, "evualuando a ", len(calificaciones), "estudiantes")
print("									")
print("Hay", cuentaAprobados, "estudiantes aprobados. Mientras hay ", cuentaReprobados, "reprobados")
print("									")
print("Las calificaciones ingresadas fueron: ", calificaciones)
print("									")

#						FIN DEL PROGRAMA
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




















