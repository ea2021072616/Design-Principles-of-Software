from notifiers.email_notifier import EmailNotifier
from notifiers.sms_notifier import SMSNotifier
from notification_service import NotificationService

def main():
    email_service = NotificationService(EmailNotifier())
    sms_service = NotificationService(SMSNotifier())

    email_service.notify("Welcome to our platform!")
    sms_service.notify("Your verification code is 123456.")

if __name__ == "__main__":
    main()
