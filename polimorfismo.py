class vehiculo:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo = modelo

    def arrancar(self):
        return f"{self.marca} {self.modelo} esta arrancando"
    
class coche(vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"

class moto(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta wiliando"
    
cochee = coche("Toyota", "Corola")
motocicleta = moto("Italika",  "Sport")

print(f"coche, marca y modelo: {cochee.marca}{cochee.modelo}")
print(f"motocicleta marca y modelo: {motocicleta.marca}{motocicleta.modelo}")
