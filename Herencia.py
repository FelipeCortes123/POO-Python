#Tipo de Herencia = Simple,Jerargica
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola, estoy hablando un poco")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = notas
        self.salario = universidad

#Herencia Multiple
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'{self.habilidad}'

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad) 
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print (f'Mi habilidad es  == {super().mostrar_habilidad()} Mi nombre es : {self.nombre}') #super siempre accede a la clase padre en este caso Persona y Artista, se puede hacer con self pero esta hace referencia a la clase de si misma 




roberto = EmpleadoArtista("Roberto",43,"colombiano","Cantaaar","programador",100)

roberto.presentarse()

herencia = issubclass(Empleado,Persona) #Verificar si empleado hace parte de Persona, hereda
print(herencia)

instancia = isinstance(roberto,EmpleadoArtista) #Verificar si roberto es un objeto (instacia de clase) de EmpleadoArtista
print(instancia)

      