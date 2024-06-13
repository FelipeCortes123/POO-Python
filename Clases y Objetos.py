class Celular :
    def __init__(self,marca,modelo,camara): #def__init__ es metodo constructor, cada que se cree un objeto(instancia de clase) se ejecuta el metodo constructor
        self.marca = marca #self hace referencia a si mismo a la clase celular
        self.modelo = modelo
        self.camara = camara 

    def llamar (self): # Toda funcion dentro de una clase es un metodo, debe pasar el parametro que hace referencia a la clase 
        print(f'Estas llamando {self.modelo}')

    def cortarllamada (self):
        print(f'Llamada cortada {self.modelo}')

celular1 = Celular("Samsung","S23","48mp")
celular2 = Celular("Iphone","Pro max", "55mp")


celular1.cortarllamada()