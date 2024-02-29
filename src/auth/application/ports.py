import abc


class IClientRepository(abc.ABC):
    seen: set

    @abc.abstractmethod
    def add(self, **kw): ...

    @abc.abstractmethod
    def get(self, **kw): ...

    @abc.abstractmethod
    def list(self): ...

    # @abc.abstractmethod
    # def delete(self, **kw): ...

    @abc.abstractmethod
    def update_from_domain(self, objects): ...


class IAuthUnitOfWork(abc.ABC):
    clients: IClientRepository

    @abc.abstractmethod
    def __enter__(self): ...

    @abc.abstractmethod
    def __exit__(self, *args): ...

    @abc.abstractmethod
    def commit(self): ...

    @abc.abstractmethod
    def rollback(self): ...
