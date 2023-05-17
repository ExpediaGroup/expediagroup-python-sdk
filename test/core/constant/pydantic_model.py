from typing import Union, Literal

from pydantic import BaseModel, Extra


class PolygonPydanticModels:
    class Polygon(BaseModel, smart_union=True, extra=Extra.forbid):
        type: Literal["Polygon"]
        coordinates: list[list[int]]

    class MultiPolygon(BaseModel, smart_union=True, extra=Extra.forbid):
        type: Literal["MultiPolygon"]
        coordinates: list[list[list[int]]]

    class FloatCoordinatesPolygon(BaseModel, smart_union=True, extra=Extra.forbid):
        type: Literal["FloatCoordinatesPolygon"]
        coordinates: list[list[float]]


class TypeAliases:
    BoundingPolygon = Union[PolygonPydanticModels.Polygon, PolygonPydanticModels.MultiPolygon]


PolygonPydanticModels.Polygon.update_forward_refs()
PolygonPydanticModels.MultiPolygon.update_forward_refs()


class PolymorphicPydanticModels:
    class PolygonWrapper(BaseModel, smart_union=True):
        polygon: TypeAliases.BoundingPolygon


class PolygonDictData:
    BOUNDING_POLYGON: dict = {
        "type": "BoundingPolygon"
    }

    POLYGON: dict = {
        "type": "Polygon",
        "coordinates": [
            [1, 2],
            [3, 4]
        ]
    }

    MULTI_POLYGON: dict = {
        "type": "MultiPolygon",
        "coordinates": [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]]
        ]
    }

    FLOAT_COORDINATES_POLYGON: dict = {
        "type": "FloatCoordinatesPolygon",
        "coordinates": [
            [1.1, 2.2],
            [3.3, 4.4]
        ]
    }

    WRAPPED_POLYGON: dict = {
        "polygon": POLYGON
    }

    WRAPPED_MULTI_POLYGON: dict = {
        "polygon": MULTI_POLYGON
    }


class PolygonObjects:
    POLYGON: PolygonPydanticModels.Polygon = PolygonPydanticModels.Polygon(
        type=PolygonDictData.POLYGON["type"],
        coordinates=PolygonDictData.POLYGON["coordinates"]
    )

    MULTI_POLYGON: PolygonPydanticModels.MultiPolygon = PolygonPydanticModels.MultiPolygon(
        type=PolygonDictData.MULTI_POLYGON["type"],
        coordinates=PolygonDictData.MULTI_POLYGON["coordinates"]
    )

    WRAPPED_POLYGON: PolymorphicPydanticModels.PolygonWrapper = PolymorphicPydanticModels.PolygonWrapper(
        polygon=POLYGON
    )

    WRAPPED_MULTI_POLYGON: PolymorphicPydanticModels.PolygonWrapper = PolymorphicPydanticModels.PolygonWrapper(
        polygon=MULTI_POLYGON
    )
