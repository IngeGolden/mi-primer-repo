
valor1 = int(input("Primer numero?: "))
valor2 = int(input("Escribe tu segundo numero?: "))



print(" 1.-SUMA \n", "2.-RESTA \n","3.-MULTIPLICACION \n","4.-DIVISION \n")

operacion = int(input("Cual numero es tu operacion?: "))

if operacion == 1:
    suma = valor1 + valor2
    print("El resultado de la suma es:",suma)
elif operacion == 2:
    resta = valor1 - valor2
    print("El resultado de la resta es:",resta)
elif operacion == 3:
    multi = valor1 * valor2
    print("El resultado de la multiplicaion es:",multi)
elif operacion == 4:
    if valor2 != 0:
        division = valor1 / valor2
        print("El resultado de la división es:", division)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opcion invalida")




