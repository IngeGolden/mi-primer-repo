nombre = "Luis"
apellido = "Rios"
frase = "Hola esta es una frase"

longitud = len(frase)
print(longitud)

print(apellido[3])

palabras = frase.split()
print(palabras)

mayusculas = frase.upper()
print(mayusculas)

texto = frase.lower()
print(texto)

mensaje = "Hello, world"
print(mensaje)
cambio = mensaje.replace("Hello","marco")
print(cambio)

for x in frase:
    print(x)