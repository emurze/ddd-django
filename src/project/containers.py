from collections.abc import Callable
from functools import lru_cache

from injector import Module, Injector, provider, singleton, Binder

from apps.notifications.adapters import NotificationsAdapter
from apps.notifications.services import (
    NotificationService,
    INotificationsAdapter,
)
from apps.products.services import ProductService
from seedwork.mediator import Mediator


def singleton_provider(fn: Callable) -> Callable:
    return singleton(provider(fn))


class MainModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(INotificationsAdapter, to=NotificationsAdapter)

    @singleton_provider
    def provide_mediator(self, injector: Injector) -> Mediator:
        mediator = Mediator()
        mediator.register_command(injector, ProductService)
        mediator.register_command(injector, NotificationService)
        return mediator


@lru_cache(1)
def get_container() -> Injector:
    return _init_container()


@lru_cache(1)
def get_mediator() -> Mediator:
    container = get_container()
    return container.get(Mediator)


def _init_container() -> Injector:
    return Injector(MainModule())
