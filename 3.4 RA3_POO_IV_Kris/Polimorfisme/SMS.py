from Missatger import Missatger

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")
