#Crea un tupla de palabras
palabras = ("manzana", "banana", "cereza")
#Pregunta al Usuario
palabra_buscar = str(input("Que palabra buscas?: "))
#Verificar si esta en la tupla
if palabra_buscar in palabras:
        print("La palabra SI esta en la tupla")
        
else:
    print("La palabra NO esta en la tupla")
