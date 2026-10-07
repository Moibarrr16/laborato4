"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""

while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break  
    except ValueError:
        print("INVALIDO")

print(f" Tabla de multiplicar del {numero} ")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")