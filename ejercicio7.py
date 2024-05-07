numero = int(input("Por favor, introduce un numero entero: "))
match numero:
    case 0:
        print("El numero es un 0.")
    case numero if numero % 2 == 0:
        print("El numero es par.")
    case numero if numero % 2 == 1:
        print("El numero es impar.")
    case _:
        print("Numero no reconocido")
        
