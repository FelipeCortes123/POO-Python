from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod #Decorador para definir una clase abstracta 
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad}")


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy Estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Trabajando como {self.actividad}")



juan = Estudiante("Juan",19,"masculino","programacion")

dalto = Trabajador("Lucas",21,"masculino","programacion")

juan.presentarse()
juan.hacer_actividad()
dalto.presentarse()
dalto.hacer_actividad()
