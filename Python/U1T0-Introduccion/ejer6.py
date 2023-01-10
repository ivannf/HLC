# Acepte una lista de 5 números flotantes como entrada del usuario.

numbers = []

for i in range(0, 5): # del 0 al 4
    item = float(input(f'Introduzca el número de la posición {i}: '))
    numbers.append(item)

print(f'Lista de números: {numbers}')