calificacion = float(input("Cual es tu calificacion con numero decimal?: "))

if calificacion >= 90:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif calificacion >= 70:
    print("Has aprobado satisfactoriamente.")
elif calificacion >= 60:
    print("Has aprobado, pero necesitas mejorar un poco.")
elif calificacion < 60:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")
else:
    print("coloca un numero real")