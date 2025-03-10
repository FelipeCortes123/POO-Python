class Tanque():
    def __init__(self):
        self.combustible = 100
    
    def argegar_combustible(self,cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
    
class Auto(): #Esta clase es la que debe tener una sola responsabilidad  (primer principio solid)
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("El auto se ha movido exitosamente")

        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

tanque = Tanque()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(40)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
