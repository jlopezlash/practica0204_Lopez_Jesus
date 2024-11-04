#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
Palabra = input('Dime una palabra ').lower()
Vocales = ['a', 'e', 'i', 'o', 'u']
for Vocal in Vocales:
    Veces = 0
    for Letra in Palabra:
        if Letra == Vocal:
            Veces += 1
    print('La vocal ' + Vocal +  ' se repite ' + str(Veces) + ' veces')