a = input('¿Cuál es el primer número? ')
while a.isdigit() == False:
    print("El primer número no es un número entero. Por favor, vuelve a intentarlo.")
    a = input('¿Cuál es el primer número? ')

a = int(a)

b = input('¿Cuál es el segundo número? ')
while b.isdigit() == False:
    print("El segundo número no es un número entero. Por favor, vuelve a intentarlo.")
    b = input('¿Cuál es el segundo número? ')
b = int(b)

print(f"Las operaciones que se han realizado son: ")
# Suma
suma = a + b
print(f"La suma de {a} y {b} es {suma}.")
# Resta
resta = a - b
print(f"La resta de {a} y {b} es {resta}.")
# Multiplicación   
multiplicacion = a * b
print(f"La multiplicación de {a} y {b} es {multiplicacion}.")
# División
if b == 0:
    print("No se puede dividir entre cero.")
else:   
    division = a / b
    print(f"La división de {a} y {b} es {division}.")