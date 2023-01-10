# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, 
# devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

mul = num1 * num2
suma = num1 + num2

if mul > 1000:
    print(f'La multiplicación de {num1} y {num2} es {mul}')
else:
    print(f'La suma de {num1} y {num2} es {suma}')