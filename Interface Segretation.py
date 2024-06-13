from abc import ABC, abstractmethod
#Se pudo crear una clase trabajador con varios metodos como dormir, trabajar y comer, pero con el principio
#estos metodos se dividen en clases para que otra clase que herede y no use algunos metodos solo herede de las clases que necesita 

class Trabajador(ABC):
    
    @abstractmethod 
    def trabajar(self):
        pass

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador,Comedor,Durmiente):

    def dormir(self):
        print("El humano esta durmiendo")

    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")


class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot esta trabajando")


robot_clase = Robot()

robot_clase.trabajar()
