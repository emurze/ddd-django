from dataclasses import dataclass

from auth.application import dtos as d
from auth.application.ports.driven import IAuthUnitOfWork
from auth.application.ports.driving import IAddClientUseCase


@dataclass(frozen=True, slots=True)
class AddClientUseCase(IAddClientUseCase):
    uow: IAuthUnitOfWork

    def execute(self, dto: d.AddClientInputDto) -> d.AddClientOutputDto:
        client_data = dto.model_dump()
        with self.uow:
            client = self.uow.clients.add(**client_data)
            output_dto = d.AddClientOutputDto.model_validate(client)
            self.uow.commit()
            return output_dto

