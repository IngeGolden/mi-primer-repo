numeros = [1, 2, 3, 4, 5, 6, 7, 8]
suma = 0
for numero in numeros:
    suma += numero
    promedio = suma/ len(numeros)
    print("----------")
    print(f"El promedio de los números en la lista es: {promedio}")