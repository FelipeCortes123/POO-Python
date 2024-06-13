class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def imprimirpersona(self):
        print(f"Este es mi nombre {self.nombre} y esta es mi edad {self.edad}")


class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado


    def imprimirgrado(self):
        print(f"Este es mi grado {self.grado}") 


estudiante = Estudiante("Juan","24","10mo")
estudiante.imprimirpersona()
estudiante.imprimirgrado()