from Src.Core.Logic import Maybe
from typing import TypeVar, Generic

T = TypeVar('T')


class ImageRepo(Generic[T]):
    @classmethod
    def all(cls) -> Maybe[set]:
        raise NotImplementedError("LandsatRepo.all() not implemented")

    @classmethod
    def getById(cls, id: str) -> Maybe[dict]:
        raise NotImplementedError("LandsatRepo.get() not implemented")

    @classmethod
    def create(cls, data: T) -> bool:
        raise NotImplementedError("LandsatRepo.save() not implemented")

    @classmethod
    def delete(cls, id: str) -> int:
        raise NotImplementedError("LandsatRepo.delete() not implemented")

    @classmethod
    def update(cls, id: str, data: T) -> bool:
        raise NotImplementedError("LandsatRepo.update() not implemented")

    @classmethod
    def exists(cls, id: str) -> bool:
        raise NotImplementedError("LandsatRepo.exists() not implemented")
