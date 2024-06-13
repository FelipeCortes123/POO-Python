class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()

print(D.mro()) #saber el orden de prioridad que da python para las herencias 

C.hablar(d) #(d) la clase que recibe mas atributos, asi es mas facil llamarla a las demas clases que estan mas arriba de d 