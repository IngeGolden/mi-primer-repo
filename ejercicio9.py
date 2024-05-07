#Tipo While ejemplo
contador = 1
while contador<=0:
    print(contador)
    contador += 1
    if contador == 60:
        break

#iniciador = 10

#while iniciador>=1:
#    print(iniciador)
#    iniciador-=1

#print("Feliz año nuevo")

suma = 0
numero = int(input("Ingresa un numero entero positivo (o un numero negativo para salir): "))

while numero >= 0:
    suma += numero 
    numero = int(input("Ingresa un numero entero positivo (o un numero negativo para salir): "))
    if suma >= 10:
        break

print("La suma de los numeros ingresados es:", suma)
