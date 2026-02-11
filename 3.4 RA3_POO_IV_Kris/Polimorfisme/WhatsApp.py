from Missatger import Missatger

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")
