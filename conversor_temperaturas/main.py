
numero = ''
unidad_usada = ''

while len(numero) == 0 or unidad_usada != 'c' and unidad_usada != 'f' and unidad_usada != 'k':
    t = input('¿Cual es la temperatura? ')
    t = t.replace("º", "").strip()

    for i in range(len(t)):
        if t[i].isalpha():
            numero = t[:i]
            if numero == '':
                print('No se ha introducido un numero')
                numero = ''
                unidad_usada = ''
            unidad = t[i:].strip()
            unidad_usada = unidad[0].lower()
            print(f'La unidad es {unidad_usada}')
            if unidad_usada != 'c' and unidad_usada != 'f' and unidad_usada != 'k':
                print(f'La medida de temperatura {unidad} no es valida')
                numero = ''
                unidad_usada = ''
            break

nuevo = ''
unidad_nueva = ''
while unidad_nueva != 'c' and unidad_nueva != 'f' and unidad_nueva != 'k':
    nuevo = input('¿A que temperatura quieres convertir? ')
    unidad_nueva = nuevo.strip()[0].lower()
    if unidad_nueva != 'c' and unidad_nueva != 'f' and unidad_nueva != 'k':
        print(f'La medida de temperatura {nuevo} no es valida')
    

if len(numero) == 0:
    print('No se ha introducido un numero')
    exit()
else:
    if unidad_usada == 'c':
        if unidad_nueva == 'f':
            resultado = (float(numero) * 9/5) + 32
            print(f'{numero}°C son {resultado}°F')
        elif unidad_nueva == 'k':
            resultado = float(numero) + 273
            print(f'{numero}°C son {resultado}K')
        elif unidad_nueva == 'c':
            resultado = float(numero)
            print(f'{numero}°C son {resultado}°C')
        else:
            print('Unidad no valida')
    elif unidad_usada == 'f':
        if unidad_nueva == 'c':
            resultado = (float(numero) - 32) * 5/9
            print(f'{numero}°F son {resultado}°C')
        elif unidad_nueva == 'k':
            resultado = (float(numero) - 32) * 5/9 + 273
            print(f'{numero}°F son {resultado}K')
        elif unidad_nueva == 'f':
            resultado = float(numero)
            print(f'{numero}°F son {resultado}°F')
        else:
            print('Unidad no valida')

    elif unidad_usada == 'k':
        if unidad_nueva == 'c':
            resultado = float(numero) - 273
            print(f'{numero}K son {resultado}°C')
        elif unidad_nueva == 'f':
            resultado = (float(numero) - 273) * 9/5 + 32
            print(f'{numero}K son {resultado}°F')
        elif unidad_nueva == 'k':
            resultado = float(numero)
            print(f'{numero}K son {resultado}K')
        else:
            print('Unidad no valida')
    else:
        print(f'La medida de temperatura {unidad} no es valida')