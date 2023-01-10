# Aplicar formato a las variables mediante el método string.format().
# Escriba un programa para usar el método string.format() para formatear las siguientes tres variables 
# según la salida esperada.

totalMoney = 1000
cantidad = 3
price = 450.00
msg = 'Tengo {0} euros para comprar {1} tarjetas gráficas por {2: .2f} dólares'

print(msg.format(totalMoney,cantidad,price))