from dataclasses import dataclass


@dataclass(eq=False)
class ServiceException(Exception):
    @property
    def message(self):
        return "Service error occurred"


@dataclass(eq=False)
class CommandHandlerNotRegisteredException(ServiceException):
    command_type: type

    @property
    def message(self) -> str:
        return f"Command handler is not registered for {self.command_type}"
