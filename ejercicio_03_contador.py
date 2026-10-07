"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
vocales = "aeiouAEIOU"
frase = input("Ingrese una frase: ")
contador = 0
for letra in frase:
    if letra in vocales:
        contador += 1
print(f"La frase ingresada tiene {contador} vocales.")
