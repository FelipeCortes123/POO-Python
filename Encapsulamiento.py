# class Miclase:
#     def __init__(self):
#         self._atributo_privado = "Valor" #_variable = variable privada, se puede acceder si se quiere , __variable = mas privada, no se puede acceder
#     def __hablar(self): #Funcion segura 
#         print("Holaaaa")
# objeto = Miclase()
# print(objeto._atributo_privado)
# print(objeto.__hablar())

#--------Getters y Setters--------

class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self): #Getters
        return self._nombre
    
    def set_nombre(self,new_nombre):
        self._nombre = new_nombre

dalto = Persona("dalto",19)

nombre = dalto.get_nombre() #Se obtiene el nombre con el getter
print(nombre)

dalto.set_nombre("Pepito") #Se cambia el nombre con el setter

nombre = dalto.get_nombre() #Se obtiene el nuevo valor del nombre


print(nombre)

 