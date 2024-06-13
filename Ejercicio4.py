class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return F"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**2) #Round sirve para redondear
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Personaje("Goku",100,100)
vegeta = Personaje("Vegeta",99,99)
jiren = Personaje("Jiren",999,999)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(jireta)