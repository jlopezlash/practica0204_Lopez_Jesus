#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
Palabra = input('Dime un palindomo ')
Reversa = list(Palabra)
Palabra = list(Palabra)
Reversa.reverse()
if Reversa == Palabra:
    print(Palabra, 'es un palíndromo ')
else:
    print(Palabra, ' no es un palíndromo ')