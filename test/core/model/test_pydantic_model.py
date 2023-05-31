import unittest
from test.core.constant.pydantic_model import *

from pydantic import parse_obj_as
from pydantic.error_wrappers import ValidationError


class PydanticModelsTest(unittest.TestCase):
    def test_create_object(self):
        polygon: PolygonPydanticModels.Polygon = PolygonPydanticModels.Polygon(
            type=PolygonDictData.POLYGON["type"], coordinates=PolygonDictData.POLYGON["coordinates"]
        )

        self.assertIsNotNone(polygon)
        self.assertIsNotNone(polygon.type)
        self.assertIsNotNone(polygon.coordinates)

        self.assertTrue(isinstance(polygon, PolygonPydanticModels.Polygon))

        self.assertEqual(polygon.type, PolygonDictData.POLYGON["type"])
        self.assertEqual(polygon.coordinates, PolygonDictData.POLYGON["coordinates"])

    def test_create_object_wrong_param_types(self):
        with self.assertRaises(ValidationError):
            multi_polygon: PolygonPydanticModels.MultiPolygon = PolygonPydanticModels.MultiPolygon(type=PolygonDictData.MULTI_POLYGON["type"], coordinates=[1])

    def test_create_object_extra_param(self):
        with self.assertRaises(ValidationError):
            polygon: PolygonPydanticModels.Polygon = PolygonPydanticModels.Polygon(
                type=PolygonDictData.POLYGON["type"], coordinates=PolygonDictData.POLYGON["coordinates"], extra_field=""
            )

    def test_create_object_wrong_type_literal(self):
        with self.assertRaises(ValidationError):
            multi_polygon: PolygonPydanticModels.MultiPolygon = PolygonPydanticModels.MultiPolygon(
                type=PolygonDictData.POLYGON["type"], coordinates=PolygonDictData.MULTI_POLYGON["coordinates"]
            )

    def test_create_polymorphic_object(self):
        polygon: PolygonPydanticModels.Polygon = PolygonPydanticModels.Polygon(
            type=PolygonDictData.POLYGON["type"], coordinates=PolygonDictData.POLYGON["coordinates"]
        )

        wrapped_polygon: PolymorphicPydanticModels.PolygonWrapper = PolymorphicPydanticModels.PolygonWrapper(polygon=polygon)

        self.assertIsNotNone(wrapped_polygon)
        self.assertIsNotNone(wrapped_polygon.polygon)
        self.assertIsNotNone(wrapped_polygon.polygon.type)
        self.assertIsNotNone(wrapped_polygon.polygon.coordinates)

        self.assertTrue(isinstance(wrapped_polygon, PolymorphicPydanticModels.PolygonWrapper))
        self.assertTrue(isinstance(wrapped_polygon.polygon, PolygonPydanticModels.Polygon))

    def test_create_invalid_polymorphic_object(self):
        float_coordinates_polygon: PolygonPydanticModels.FloatCoordinatesPolygon = PolygonPydanticModels.FloatCoordinatesPolygon(
            type="FloatCoordinatesPolygon", coordinates=PolygonDictData.FLOAT_COORDINATES_POLYGON["coordinates"]
        )

        with self.assertRaises(ValidationError):
            wrapped_polygon: PolymorphicPydanticModels.PolygonWrapper = PolymorphicPydanticModels.PolygonWrapper(polygon=float_coordinates_polygon)

    def test_serialize_objects(self):
        serialized_polygon = PolygonObjects.POLYGON.dict()

        self.assertIsNotNone(serialized_polygon)
        self.assertIsNotNone(serialized_polygon["type"])
        self.assertIsNotNone(serialized_polygon["coordinates"])

        self.assertEqual(serialized_polygon, PolygonDictData.POLYGON)

    def test_deserialize_object(self):
        deserialized_polygon = parse_obj_as(PolygonPydanticModels.Polygon, PolygonDictData.POLYGON)

        self.assertIsNotNone(deserialized_polygon)
        self.assertIsNotNone(deserialized_polygon.type)
        self.assertIsNotNone(deserialized_polygon.coordinates)

        self.assertTrue(isinstance(deserialized_polygon, PolygonPydanticModels.Polygon))

        self.assertEqual(deserialized_polygon, PolygonObjects.POLYGON)

    def test_test_deserialize_object_invalid_data(self):
        with self.assertRaises(ValidationError):
            deserialized_polygon = parse_obj_as(PolygonPydanticModels.MultiPolygon, PolygonDictData.POLYGON)

    def test_deserialize_polymorphic_object(self):
        # Case 1
        wrapped_polygon: PolymorphicPydanticModels.PolygonWrapper = parse_obj_as(PolymorphicPydanticModels.PolygonWrapper, PolygonDictData.WRAPPED_POLYGON)

        self.assertIsNotNone(wrapped_polygon)
        self.assertIsNotNone(wrapped_polygon.polygon)
        self.assertIsNotNone(wrapped_polygon.polygon.type)
        self.assertIsNotNone(wrapped_polygon.polygon.coordinates)

        self.assertTrue(isinstance(wrapped_polygon, PolymorphicPydanticModels.PolygonWrapper))
        self.assertTrue(isinstance(wrapped_polygon.polygon, PolygonPydanticModels.Polygon))

        # Case 2
        wrapped_multi_polygon: PolymorphicPydanticModels.PolygonWrapper = parse_obj_as(
            PolymorphicPydanticModels.PolygonWrapper, PolygonDictData.WRAPPED_MULTI_POLYGON
        )

        self.assertIsNotNone(wrapped_multi_polygon)
        self.assertIsNotNone(wrapped_multi_polygon.polygon)
        self.assertIsNotNone(wrapped_multi_polygon.polygon.type)
        self.assertIsNotNone(wrapped_multi_polygon.polygon.coordinates)

        self.assertTrue(isinstance(wrapped_multi_polygon, PolymorphicPydanticModels.PolygonWrapper))
        self.assertTrue(isinstance(wrapped_multi_polygon.polygon, PolygonPydanticModels.MultiPolygon))
