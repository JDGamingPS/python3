nota = int(input('proporciona la nota entre 0 y 10: '))

if 9 <= nota <= 10:
    print('A')
elif 8 <= nota < 9:
    print('B')
elif 7 <= nota < 8:
    print('C')
elif 6 <= nota < 7:
    print('D')
elif 0 <= nota < 6:
    print('F')
else:
    print('Valor Desconocido')