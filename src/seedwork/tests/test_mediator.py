from dataclasses import dataclass

import pytest
from faker import Faker
from injector import Injector

from seedwork.mediator import Mediator, command_handler


@dataclass(frozen=True)
class CreateProductCommand:
    title: str


@dataclass(frozen=True)
class UpdateProductCommand:
    title: str


@dataclass(frozen=True)
class ProductService:
    mediator: Mediator

    @command_handler
    def create_product(self, command: CreateProductCommand) -> str:
        return f"Product {command.title} created"

    @command_handler
    async def update_product(self, command: UpdateProductCommand) -> str:
        return f"Product {command.title} updated"


@pytest.mark.unit
async def test_mediator_register_command_success(faker: Faker) -> None:
    container = Injector()
    mediator = Mediator()
    mediator.register_service_commands(container, ProductService)

    title = faker.text(max_nb_chars=50)
    command = CreateProductCommand(title=title)
    res = mediator.handle(command)

    command2 = UpdateProductCommand(title=title)
    res2 = await mediator.handle(command2)

    assert res == f"Product {command.title} created"
    assert res2 == f"Product {command2.title} updated"
