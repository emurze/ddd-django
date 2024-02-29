import abc

from auth.application import dtos as d


class IAddClientUseCase(abc.ABC):
    @abc.abstractmethod
    def execute(self, dto: d.AddClientInputDto) -> d.AddClientOutputDto:
        ...


class IGetClientUseCase:
    pass


class IGetClientsUseCase:
    pass


class IUpdateClientsUseCase:
    pass


class IDeleteClientsUseCase:
    pass
