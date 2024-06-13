# #Principio de sustitucion de liskov

# class Ave:
#     def volar(self):
#         return "Estoy Volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo Volar"
    
# def hacer_volar(ave = Ave):
#     return ave.volar()


# print(hacer_volar(Pinguino()))

class FormaGeometrica:
    def area(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def area(self):
        return self.ancho * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado) #Hereda de la superclase rectangulo, para eso se usa el super()

