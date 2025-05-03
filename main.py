escala = 0
estudiantes = input("Cúantos estudiantes quieres evualuar? pueden ser un máximo de 100: ")
calificaciones = input("Ingresa las calificaciones de los estudiantes, separas con un espacio: ").split()

print(len(calificaciones))
print(calificaciones)

if len(calificaciones) > 100:
	print("sí")
