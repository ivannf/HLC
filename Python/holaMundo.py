print('Hola Mundo!')

# Este es mi primer comentario

nombre = input('Introduzca su nombre por pantalla: ')
# nombre = 'Ivan'
# print('Hola,', nombre, ', eres buena gente')
print(f'Hola {nombre}, eres buena gente')

nota = int(input('Introduce la nota del alumno: '))

if nota < 5:
    print('Suspenso')
else:
    print('Aprobado')