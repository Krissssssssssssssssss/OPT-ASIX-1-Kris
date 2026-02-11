from Missatger import Missatger

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant Email: {missatge}")
