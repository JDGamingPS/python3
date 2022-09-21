print('Proporcione los siguientes datos del libro:')
nombre = input('Proporcione el nombre: ')
id = int(input('Proporcione el ID: '))
precio = float(input('Proporcione el precio: '))
envio = bool(input('Indica si el envio es gratuito (True/False): '))

print(f'nombre: {nombre} \n Id: {id} \n Precio: {precio} \n Envio: {envio}')