from Src.Core.Infra.Mapper import Mapper as ContractMapper
from Src.Domain.Entities.Image import Image
from Src.Infra.Database.InMemory.ImageRepo import RawImage


class ImageMapper(ContractMapper[Image, RawImage]):
    @staticmethod
    def toInfra(entity: Image) -> RawImage:
        return {
            'id': entity.id(),
            'date_acquired': entity.dateAcquired(),
            'azimuth': entity.azimuth(),
            'sun_elevation': entity.sunElevation()
        }

    @staticmethod
    def toDomain(raw: RawImage) -> Image:
        return Image.create({
            'date': raw['date_acquired'],
            'azimuth': raw['azimuth'],
            'sun_elevation': raw['sun_elevation']
        }, raw['id'])
