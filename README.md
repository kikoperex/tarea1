##Especificaciones Técnicas para la Implementación de un Sistema de Análisis de
##Calificaciones de Estudiantes
###Objetivo:
Desarrollar un sistema que permita gestionar las calificaciones de un grupo de estudiantes,
calcular el promedio de las calificaciones, determinar cuántos estudiantes aprobaron y cuántos no
aprobaron, y visualizar los resultados de manera clara y precisa.
#1. Requerimientos Funcionales
##Entrada de Datos:
###1. Número de estudiantes: El sistema debe permitir que el usuario ingrese la cantidad de
estudiantes cuyos datos serán procesados. Este valor debe ser un número entero positivo
que no exceda los 100 estudiantes.
###2. Calificaciones de los estudiantes: Para cada estudiante, el sistema debe permitir al
usuario ingresar una calificación numérica (real o entera). Las calificaciones deben estar
dentro de un rango válido, dependiendo de la escala que se utilice:
o Escala 0-10: Las calificaciones deben estar en el rango de 0 a 10, inclusive.
o Escala 0-100: Las calificaciones deben estar en el rango de 0 a 100, inclusive.
###3. Validación de entrada:
o El sistema debe verificar que el número de estudiantes no supere el máximo
establecido (100 estudiantes).
o Las calificaciones deben ser ingresadas como números válidos dentro del rango
de 0 a 10 (o 0 a 100), y se deben manejar adecuadamente los posibles errores de
entrada (como caracteres no numéricos).
##Proceso de Cálculo:
###1. Promedio de las calificaciones:
El sistema debe calcular el promedio de las calificaciones ingresadas, sumando todas las
calificaciones y dividiendo por el número total de estudiantes.
###2. Determinación de Aprobación:
Para cada estudiante, el sistema debe determinar si su calificación es suficiente para
aprobar. El umbral de aprobación debe estar definido como:
o Escala 0-10: Aprobar si la calificación es mayor o igual a 6.
o Escala 0-100: Aprobar si la calificación es mayor o igual a 60.
El sistema debe contar cuántos estudiantes aprobaron y cuántos no aprobaron.
###3. Visualización de Resultados:
o El sistema debe mostrar el promedio de las calificaciones.o
o
El sistema debe mostrar la cantidad de estudiantes que aprobaron y los que no
aprobaron.
El sistema debe mostrar una lista con todas las calificaciones ingresadas.
##2. Requerimientos No Funcionales
###Usabilidad:


El sistema debe ser interactivo y fácil de usar, con una interfaz basada en texto que guíe
al usuario en el proceso de entrada de datos.
Las instrucciones deben ser claras y concisas, indicando al usuario qué tipo de datos debe
ingresar y en qué formato.
###Desempeño:


El sistema debe ser capaz de procesar los datos de hasta 100 estudiantes de manera
eficiente y rápida. Aunque se trata de una cantidad relativamente pequeña de datos, se
debe garantizar que el programa se ejecute sin demoras innecesarias.
El tiempo de respuesta para las operaciones de entrada y salida debe ser inmediato.
###Manejo de Errores:


Errores de entrada: El sistema debe manejar de manera adecuada los errores de entrada
del usuario, como calificaciones fuera de rango, caracteres no numéricos, o entradas
vacías.
Mensajes de error: Los mensajes de error deben ser claros y deben indicar al usuario
cómo corregir la entrada.
###Escalabilidad:

Aunque la implementación está diseñada para un máximo de 100 estudiantes, el sistema
debe ser escalable para manejar una mayor cantidad de datos sin necesidad de reescribir
el código. Esto puede lograrse mediante el uso de arreglos dinámicos o estructuras de
datos más complejas si es necesario en el futuro.
##3. Diseño del Sistema
###Estructura de Datos:
1. Arreglos:
El sistema utilizará un arreglo para almacenar las calificaciones de los estudiantes. Dado
que el número máximo de estudiantes es 100, el arreglo puede tener un tamaño fijo. Si elnúmero de estudiantes excede este límite, el sistema debería rechazar la entrada o
permitir el redimensionamiento dinámico.
o Arreglo de calificaciones: Un arreglo de tipo float o int (dependiendo de la
escala de calificación) almacenará las calificaciones de los estudiantes.
o Variables de conteo: Se utilizarán variables para contar la cantidad de
estudiantes que aprobaron y los que no aprobaron.
Ejemplo de declaración en C++:
const int MAX_ESTUDIANTES = 100;
float calificaciones[MAX_ESTUDIANTES];
int aprobados = 0, reprobados = 0;
###Lógica de Cálculo:
1. Promedio: Para calcular el promedio de las calificaciones, se sumarán todas las
calificaciones y luego se dividirá entre el número de estudiantes.
2. Aprobación: Para verificar si un estudiante aprobó, se utilizará una estructura de control
if para comparar la calificación con el umbral de aprobación:
###Estructuras de Control:
1. Estructuras Iterativas:
o Se utilizará un ciclo for para recorrer las calificaciones ingresadas y realizar los
cálculos necesarios (promedio y aprobación).
o El ciclo debe ejecutarse desde el primer hasta el último estudiante (índices del
arreglo).
2. Estructuras Condicionales:
o Se utilizará un if para verificar si cada estudiante ha aprobado o reprobado, con
base en su calificación.
###Entrada/Salida:


La entrada debe ser gestionada mediante el uso de cin para ingresar el número de
estudiantes y las calificaciones de cada uno.
La salida debe mostrarse utilizando cout para imprimir el promedio, la cantidad de
aprobados y reprobados, y la lista de calificaciones.
##4. Flujo de Trabajo del Sistema
###1. Ingreso de datos:
o El sistema solicita al usuario el número de estudiantes.
o Luego, el sistema solicita las calificaciones de cada estudiante, validando que se
ingresen valores numéricos dentro del rango permitido.
###2. Cálculo:o
o
El sistema calcula el promedio de las calificaciones.
El sistema determina cuántos estudiantes aprobaron y cuántos no aprobaron.
###3. Visualización:
o El sistema muestra el promedio general.
o El sistema muestra la cantidad de estudiantes que aprobaron y los que no
aprobaron.
o El sistema imprime todas las calificaciones ingresadas.
##5. Restricciones y Consideraciones



El sistema debe ser diseñado para manejar una cantidad máxima de 100 estudiantes.
Las calificaciones deben ser ingresadas de forma correcta y estar dentro del rango
especificado.
Los errores de entrada deben ser manejados de manera que el sistema sea robusto frente a
entradas inválidas.
##6. Casos de Uso
###1. Caso de uso principal:
o Un usuario ingresa el número de estudiantes.
o El usuario ingresa las calificaciones de cada estudiante.
o El sistema calcula el promedio, cuenta los aprobados y reprobados, y muestra los
resultados.
###2. Caso de error:
o El usuario ingresa un valor no numérico o una calificación fuera de rango.
o El sistema muestra un mensaje de error y solicita que el usuario ingrese un valor
válido.
##7. Posibles Mejoras (Futuras Extensiones)



Implementar el uso de estructuras de datos avanzadas como struct para almacenar no
solo las calificaciones, sino también el nombre del estudiante y otras características.
Ampliar el sistema para permitir que los estudiantes ingresen sus datos de manera
interactiva a través de una interfaz gráfica.
Incorporar un sistema de autenticación para garantizar que solo los estudiantes
registrados ingresen sus calificaciones.
