class Animal:
    def comer(self):
        print("Comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantar")
    
class Ave(Animal):
    def volar(self):
        print("Volando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())
