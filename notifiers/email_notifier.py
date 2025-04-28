from .notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"📧 Email sent: {message}")
