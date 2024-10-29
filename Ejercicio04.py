#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
Loterias = []
for i in range(8):
    Loterias.append(int(input('Cuales es el número ganador ')))
Loterias.sort()
print('Los números ganadores són ' + str(Loterias))