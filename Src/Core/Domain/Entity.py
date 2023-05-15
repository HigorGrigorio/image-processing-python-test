from uuid import uuid4
from .Contracts.Equable import Equable
from typing import TypeVar

TProps = TypeVar('TProps')


class Entity(Equable):
    def __init__(self, props: TProps, id: str | None = None):
        self.__id = id or uuid4()
        self.__props = props

    def id(self):
        return self.__id

    def props(self) -> TProps:
        return self.__props

    def equals(self, other):
        if not isinstance(other, Entity):
            return False
        return self.props() == other.props() or self.__id == other.id()

    def __eq__(self, other):
        return self.equals(other)

    def __hash__(self):
        return hash(self.id())
