class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)
