from Src.Core.Logic import Maybe
from Src.Infra.Database.Contracts.ImageRepo import ImageRepo as ContractRepo
from Src.Infra.Database.Dtos.Image import RawImage


class InMemoryImageRepo(ContractRepo):
    dataset: dict[RawImage] = {}

    """
        Gets all entities on data frame.
        
        :return: All images.
    """

    @classmethod
    def all(cls) -> Maybe[list[RawImage]]:
        data = list(cls.dataset.items())

        if len(data) == 0:
            return Maybe.nothing()
        return Maybe.just(data)

    @classmethod
    def getById(cls, id: str) -> Maybe[RawImage]:
        if id in cls.dataset:
            return Maybe.just(cls.dataset[id])
        return Maybe.nothing()

    @classmethod
    def create(cls, data: RawImage) -> bool:
        if data['id'] in cls.dataset:
            return False
        cls.dataset[data['id']] = data
        return True

    @classmethod
    def delete(cls, id: str) -> int:
        if id in cls.dataset:
            del cls.dataset[id]
            return 1
        return 0

    @classmethod
    def update(cls, id: str, data: RawImage) -> bool:
        if id in cls.dataset:
            cls.dataset[id] = data
        return False

    @classmethod
    def exists(cls, id: str) -> bool:
        return id in cls.dataset
