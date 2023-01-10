# Acepte tres cadenas cualquiera de una llamada input(). Escriba un programa para 
# tomar tres nombres como entrada de un usuario con una única llamada a función input().

cadena = input('Introduce los tres nombres de usuario que desea: ')
x = cadena.split(' ')

nombre1 = x[0]
nombre2 = x[1]
nombre3 = x[2]

print(f'El primer nombre es {nombre1}, el segundo es {nombre2} y el tercero es {nombre3}')