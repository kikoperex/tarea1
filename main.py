# > <
#------------------------------------------------------------------------------------------------

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
		evaluaciónEscala = 1
		correcto = True

	elif escala == "2":
		evaluaciónEscala = 2
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

while correcto == False:
	calificaciones = input("Ingresa las calificaciones de los estudiantes, separas con un espacio: ").split()


	print(len(calificaciones))
	print(calificaciones)
	c = 0
	while c < len(calificaciones):
		calificaciones[c] = int(calificaciones[c])
		print(calificaciones[0] + c, "ESTE ES EL CERO", c)
#		print(c, calificaciones[c] + 1)
		c = c + 1

	res = all(ele == int for ele in calificaciones)
	print(res)

	if len(calificaciones) > 100:
		print("sí")
