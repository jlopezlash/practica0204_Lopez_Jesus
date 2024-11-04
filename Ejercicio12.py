#Escribir un programa que pregunte por una muestra de números, separados por comas,
#los guarde en una lista y muestre por pantalla su media y desviación típica.
Números = input('Dime números, separados por comas ')
Números = Números.split(',')
c = len(Números)
for i in range(c):
    Números[i] = int(Números[i])
Números = list(Números)
a = 0
b = 0
for i in Números:
    a += i
    b += i**2
media = a/c
dt = (b/c-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', dt)