#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
Asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
Aprobadas = []
for Asignatura in Asignaturas:
    Nota = int(input('¿Qué nota has sacado en Asignaturas ' + Asignatura + '? '))
    if Nota >=5:
        Aprobadas.append(Asignatura)
for Asignatura in Aprobadas:
        Asignaturas.remove(Asignatura)
print('Tienes que repetír', Asignaturas)
