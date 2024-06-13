#Depender de clases de alto nivel, estas deben estar independientes ya que abarcan gran parte de la logica 
#Este ejercicio viola la ley de dependencia, ya que la clase diccionario no es la principal y corrector esta heredando de ellas
# class Diccionario:
#     def verificar_palabra(self,palabra):
        
#         pass

# class Corrector():
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self,texto):

#         pass
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador

    def corregir_texto(self,texto):
        pass

corrector = CorrectorOrtografico(VerificadorOrtografico)
