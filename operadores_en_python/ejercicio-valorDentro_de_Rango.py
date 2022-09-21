#operador and
valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

print(dentroRango)

if dentroRango:
    print(f'el valor {valor} esta dentro del rango')
else:
    print(f'el valor {valor} esta fuera del rango')

#operador "or"

vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print('Puede asistir al juego de su hijo')
else:
    print('tiene deberes por hacer')

#operador not

if not (vacaciones or diaDescanso):
    print('tiene deberes por hacer')
else:
    print('Puede asistir al juego de su hijo')

#Rango de edades 20's y 30's
edad = int(input('Introduce u edad: '))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    #print('dentro del rango (20\´s) o 30\`s')
    if veintes:
        print('dentro de los 20s')
    elif treintas:
        print('Dentro de los 30s')
    else:
        print('fuera de rango')
else:
    print("No esta dentro de los 20's o 30`s")

#simplificando

if (20 <= edad < 30) or (30 <= edad < 40):
    print('dentro de los 20s')
else:
    print('Dentro de los 30s')