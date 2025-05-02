import re

tasas_de_cambio = {
    'EUR': {'USD': 1.1, 'JPY': 130.0, 'MXN': 20.0},
    'USD': {'EUR': 0.9, 'JPY': 120.0, 'MXN': 18.0},
    'JPY': {'EUR': 0.0077, 'USD': 0.0083, 'MXN': 0.15},
    'MXN': {'EUR': 0.05, 'USD': 0.056, 'JPY': 6.7}
}

moneda_inicial = input('¿De qué moneda quieres convertir? ')
while moneda_inicial not in tasas_de_cambio:
    print('La moneda inicial no es válida. Las monedas admitidas son: EUR, USD, JPY, MXN')
    moneda_inicial = input('¿De qué moneda quieres convertir? ')

moneda_final = input('¿A qué moneda quieres convertir? ')
while moneda_final not in tasas_de_cambio:
    print('La moneda final no es válida. Las monedas admitidas son: EUR, USD, JPY, MXN')
    moneda_final = input('¿A qué moneda quieres convertir? ')

cantidad = input('¿Cuánto dinero quieres convertir? ')
cantidad_limpia = re.sub(',', '', cantidad)

# Validar que el número es positivo y decimal válido
while not cantidad_limpia.replace('.', '', 1).isdigit() or float(cantidad_limpia) <= 0:
    print('La cantidad debe ser un número positivo válido.')
    cantidad = input('¿Cuánto dinero quieres convertir? ')
    cantidad_limpia = re.sub(',', '', cantidad)

cantidad = float(cantidad_limpia)

def convertir_moneda(cantidad, moneda_inicial, moneda_final):
    cantidad = float(cantidad)
    tasa = tasas_de_cambio[moneda_inicial][moneda_final]
    return cantidad * tasa

resultado = convertir_moneda(cantidad, moneda_inicial, moneda_final)
print(f'{cantidad:.2f} {moneda_inicial} son {resultado:.2f} {moneda_final}')    