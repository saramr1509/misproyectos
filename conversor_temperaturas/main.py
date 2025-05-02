
numero = ''
unidad_usada = ''

while len(numero) == 0 or unidad_usada not in ['c', 'f', 'k']:
    t = input('¿Cual es la temperatura? ')
    t = t.replace("º", "").strip()

    for i in range(len(t)):
        if t[i].isalpha():
            numero = t[:i]
            unidad = t[i:].strip()
            unidad_usada = unidad[0].lower()
            if numero == '':
                print('No se ha introducido un numero')
                numero = ''
                unidad_usada = ''
            elif unidad_usada not in ['c', 'f', 'k']:
                print(f'La medida de temperatura {unidad} no es valida')
                numero = ''
                unidad_usada = ''
            break
    else:
        # No se encontró ninguna letra (unidad)
        print('No se ha introducido una unidad válida')
        numero = ''
        unidad_usada = ''

nuevo = ''
unidad_nueva = ''
while unidad_nueva not in ['c', 'f', 'k']:
    nuevo = input('¿A que temperatura quieres convertir? ')
    unidad_nueva = nuevo.strip()[0].lower()
    if unidad_nueva not in ['c', 'f', 'k']:
        print(f'La medida de temperatura {nuevo} no es valida')

# Conversión
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
