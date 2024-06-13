class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #Como devolver los datos en una cadena de texto 
        return f'Persona(nombre = {self.nombre},edad = {self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})' #Las comillas para datos tipo string en la funcion repr
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

juan = Persona("juan",19)

pedro = Persona("pedro",30)

nueva_persona = juan + pedro
print(nueva_persona.edad) 


