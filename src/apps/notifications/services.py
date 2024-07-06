import abc
from dataclasses import dataclass

from seedwork.mediator import command_handler


class INotificationsAdapter(abc.ABC):
    @abc.abstractmethod
    def send_message_to_client(self, message: str): ...


@dataclass(frozen=True)
class SendMessageToClientCommand:
    message: str


class NotificationService:
    notifications_adapter: INotificationsAdapter

    @command_handler
    def send_message_to_client(
        self, command: SendMessageToClientCommand
    ) -> None:
        self.notifications_adapter.send_message_to_client(command.message)
