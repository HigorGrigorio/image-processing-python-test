from typing import TypedDict


class RawImage(TypedDict):
    id: str
    date_acquired: str
    azimuth: float
    sun_elevation: float
