class Gato():
    def sonido(self):
        print('miau')

class Perro():
    def sonido(self):
        print('guau')

#Misma funcion diferente clase y diferente ejecucion

def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()

perro = Perro()


print(perro.sonido())

