from dataclasses import dataclass

from apps.notifications.services import SendMessageToClientCommand
from seedwork.mediator import Mediator, command_handler


@dataclass(frozen=True)
class CreateProductCommand:
    title: str


@dataclass(frozen=True)
class UpdateProductCommand:
    title: str


@dataclass(frozen=True)
class DeleteProductCommand:
    product_id: int


@dataclass(frozen=True)
class ProductService:
    mediator: Mediator
    # uow: IUnitOfWork  # TODO: Encapsulated Unit of work

    @command_handler
    def create_product(self, command: CreateProductCommand) -> None:
        message = f"<Your {command.title} product is already in stock>"
        self.mediator.handle(SendMessageToClientCommand(message))
        # TODO: self.mediator.delay()

    @command_handler
    def update_product(self, command: UpdateProductCommand):
        pass

    @command_handler
    def delete_product(self, command: DeleteProductCommand):
        pass
