from typing import TypeVar, Generic
from Src.Core.Logic import Result

T = TypeVar('T')


class Service(Generic[T]):
    def execute(self, data: T) -> Result:
        raise NotImplementedError('execute method must be implemented')
