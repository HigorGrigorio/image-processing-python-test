from Src.Domain.Validators.ImageValidator import ImageValidator as Validator
from Src.Core.Domain.Entity import Entity
from typing import TypedDict


class ImageProps(TypedDict):
    date_acquired: str
    azimuth: float
    sun_elevation: float


class Image(Entity):
    def __init__(self, props: ImageProps, id: str = None):
        super().__init__(props, id)

    def __str__(self):
        return f'Image: {self.id()}: {self.props()}'

    def dateAcquired(self) -> str:
        return super().props()['date_acquired']

    def azimuth(self) -> float:
        return super().props()['azimuth']

    def sunElevation(self) -> float:
        return super().props()['sun_elevation']

    def equals(self, other):
        if not isinstance(other, Image):
            return False
        return super().equals(other)

    # @staticmethod
    # def rules() -> dict[str, str]:
    #     return {
    #         'date_acquired': 'required',
    #         'azimuth': 'required|numeric',
    #         'sun_elevation': 'required|numeric'
    #     }
    #
    # @staticmethod
    # def messages() -> dict[str, str]:
    #     return {
    #         'date_acquired.required': 'Date is required',
    #         'azimuth.required': 'Azimuth is required',
    #         'azimuth.numeric': 'Azimuth must be numeric',
    #         'sun_elevation.required': 'Sun elevation is required',
    #         'sun_elevation.numeric': 'Sun elevation must be numeric'
    #     }

    @staticmethod
    def create(props: dict, id: str = None):
        return Image(Validator.create(props).validate(), id)
