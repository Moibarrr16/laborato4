"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""
numero_secreto = 7 
while True: 
    numero_usuario = int(input("Adivina el número (entre 1 y 10): "))
    if numero_usuario < numero_secreto:
        print("El número es mayor. Intenta de nuevo.") 
    elif numero_usuario > numero_secreto:   
        print("El número es menor. Intenta de nuevo.")
    else:   
        print("Adivinaste el número")
        break
