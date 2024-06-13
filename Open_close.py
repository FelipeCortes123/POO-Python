#Este principio las clases, modulos,etc. Deben estar abiertas para la extension y cerrada para la modificación
#No modificar clases si no agregar clases para adicionar sobre la clase (herencia)
class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class Notificadoremail(Notificador):
    def Notificar(self):
        print(f"Enviando Mensaje a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviadno SMS a {self.usuario.sms}")

class NotificadorWhatssapp(Notificador):
    def Notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatssapp}")
        