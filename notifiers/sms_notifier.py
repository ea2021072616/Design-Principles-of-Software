from .notifier import Notifier

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"📱 SMS sent: {message}")
