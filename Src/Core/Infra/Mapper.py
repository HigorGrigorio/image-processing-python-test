from typing import TypeVar, Generic

TDomain = TypeVar('TDomain')
TInfra = TypeVar('TInfra')


class Mapper(Generic[TDomain, TInfra]):
    @staticmethod
    def toDomain(raw: TInfra) -> TDomain:
        raise NotImplementedError("Mapper.toDomain() not implemented")

    @staticmethod
    def toInfra(entity: TDomain) -> TInfra:
        raise NotImplementedError("Mapper.toInfra() not implemented")
