#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
#que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for Letras in range(len(ABC), 1,-1):
    if Letras %3 == 0:
        ABC.pop(Letras-1)
print(ABC)
