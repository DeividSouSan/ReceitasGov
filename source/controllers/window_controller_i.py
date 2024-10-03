from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from views.base_view import BaseView


class WindowControllerI(ABC):
    @abstractmethod
    def create_window(self) -> None:
        pass

    @abstractmethod
    def switch_theme(self, theme: str) -> None:
        pass

    @abstractmethod
    def set_views(self, view: list[Type["BaseView"]]) -> None:
        pass

    @abstractmethod
    def get_view(self, view_name: str) -> None:
        pass
