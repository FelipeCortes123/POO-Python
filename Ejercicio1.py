class Estudiante :
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando............")



nombre = input("Digite su nombre: ")
edad = input("Su edad: ")
grado = input("Ahora su grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
    Datos del estudiante: \n
    Nombre : {estudiante.nombre}\n
    Edad : {estudiante.edad} \n
    Grado : {estudiante.grado}\n

 """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
