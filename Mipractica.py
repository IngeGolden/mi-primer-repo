#case
numero = int(input("Que caso necesitas?: "))
match numero:
    case 1:
        print("robot 1")
    case 2:
        print("robot 2")
    case 3:
        print("robot 3")
    case _:
        print("Numero no reconocido")