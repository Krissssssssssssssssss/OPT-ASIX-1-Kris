

from abc import ABC, abstractmethod



# Interfície Notificador

class Notificador(ABC):
    @abstractmethod
    def enviar(self, missatge):
        pass

# Implementacions concretes

class EmailNotificador(Notificador):
    def enviar(self, missatge):
        print(f" Enviant email: {missatge}")


class SMSNotificador(Notificador):
    def enviar(self, missatge):
        print(f" Enviant SMS: {missatge}")

# Classe Comanda (baix acoblament)

class Comanda:
    def __init__(self, client, notificador: Notificador):
        self.client = client
        self.notificador = notificador  # Dependència injectada

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(
            f"Hola {self.client}, la teva comanda ha estat confirmada."
        )

# Exemple d'ús

if __name__ == "__main__":
    # Canvi de notificador sense tocar Comanda
    email = EmailNotificador()
    comanda1 = Comanda("Laura", email)
    comanda1.confirmar()

    sms = SMSNotificador()
    comanda2 = Comanda("Marc", sms)
    comanda2.confirmar()