from typing import TypeVar, Generic

T = TypeVar('T')


class Factory(Generic[T]):
    def create(self) -> T:
        raise NotImplementedError('create method must be implemented')
