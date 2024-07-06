from apps.notifications.services import INotificationsAdapter


class NotificationsAdapter(INotificationsAdapter):
    def send_message_to_client(self, message) -> None:
        print("SEND MESSAGE TO CLIENT")
