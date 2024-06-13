def decorador(funcion):
    def funcion_modificada():
        print("Antes")
        funcion()
    return funcion_modificada

# def saludo():
#     print("Hola juan")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador #nombre de la funcion 
def saludo():
    print("Hola como andas")

saludo() 