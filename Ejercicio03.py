#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
#y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
#es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
Asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
Notas = []
for Asignatura in Asignaturas:
    Nota = input('¿Qué nota has sacado en Asignaturas ' + Asignatura + '? ')
    Notas.append(Nota)
for i in range(len(Asignaturas)):
    print('En ', Asignaturas[i], 'tu nota es ', Notas[i])