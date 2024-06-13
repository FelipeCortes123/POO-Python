class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property  #Decorador para que esta funcion sea una propiedad, accede (getter)
    def get_nombre(self):
        return self.__nombre
    
    @get_nombre.setter #Decorador para cambiar una variable
    def get_nombre(self,new_nombre):
        self.__nombre = new_nombre

    @get_nombre.deleter #Decorador para eliminar
    def nombre(self):
        del self.__nombre 
 
dalto = Persona("dalto",19)

nombre = dalto.get_nombre #Con el @property se puede acceder como una propiedad, osea sin ()
print(nombre)

dalto.get_nombre = "Juan" #Cambiamos la variable

print(nombre)

del dalto.nombre #Elimina la variable

print("Maquinaaa")