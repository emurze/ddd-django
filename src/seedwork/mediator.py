import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, TypeAlias, TypeVar

from injector import Injector, inject

from seedwork.exceptions import CommandHandlerNotRegisteredException

TF = TypeVar("TF", bound=Callable)
Command: TypeAlias = Any


def command_handler(func: TF) -> TF:
    func._is_command_handler = True
    return func


def get_first_argument_annotation(func: Callable) -> Any:
    signature = inspect.signature(func)
    parameters = list(signature.parameters.values())

    if not parameters:
        # TODO: custom exception
        raise ValueError("The function has no arguments.")

    first_param = parameters[0]
    annotation = first_param.annotation

    if (
        annotation is inspect._empty
    ):  # TODO: fix Cannot find reference '_empty' in 'inspect.pyi'
        # TODO: custom exception
        raise TypeError("No annotation for the first parameter.")

    return annotation


@dataclass(frozen=True)
class Mediator:
    command_map: dict[type[Command], Callable] = field(default_factory=dict)

    def register_command(
        self,
        command_type: type[Command],
        _command_handler: Callable,
    ) -> None:
        self.command_map[command_type] = _command_handler

    def register_service_commands(
        self,
        container: Injector,
        service_type: Any,
    ) -> None:
        # inject dependencies to service
        service = container.get(inject(service_type))
        methods = inspect.getmembers(service, inspect.ismethod)

        for _, method in methods:
            if not hasattr(method, "_is_command_handler"):
                continue

            command_type = get_first_argument_annotation(method)
            self.register_command(command_type, method)

    def handle(self, command: Command) -> Any:
        command_type = type(command)
        handler = self.command_map[command_type]

        if not handler:
            raise CommandHandlerNotRegisteredException(command_type)

        return handler(command)
