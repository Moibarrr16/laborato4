import math

def area_circulo(radio):
    # Calcula el área (π * r^2) y muestra el resultado
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area:.2f}\n")

def area_triangulo(base, altura): 
    # Calcula el área ((base * altura) / 2) y muestra el resultado
    area = (base * altura) / 2
    print(f"El área es: {area:.2f}\n")

def perimetro_rectangulo(base, altura):
    # Calcula el perímetro (2 * (base + altura)) y muestra el resultado
    perimetro = 2 * (base + altura)
    print(f"El perímetro del rectángulo es: {perimetro}\n")

def menu():
    activo = True
    while activo:
        print("CALCULADORA GEOMÉTRICA")
        print("1. Área de un Círculo")
        print("2. Área de un Triángulo")
        print("3. Perímetro de un Rectángulo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        match opcion:
            case "1":
                x = float(input("Ingrese el radio del círculo: "))
                area_circulo(x)
            case "2":
                x = float(input("Ingrese la base: "))
                y = float(input("Ingrese la altura: "))
                area_triangulo(x, y)
            case "3":
                x = float(input("Ingrese la base del rectángulo: "))
                y = float(input("Ingrese la altura del rectángulo: "))
                perimetro_rectangulo(x, y) 
            case "4":
                print("Saliendo del programa...")
                activo = False
            case _:
                print("Opción inválida. Intente de nuevo.\n")

menu()