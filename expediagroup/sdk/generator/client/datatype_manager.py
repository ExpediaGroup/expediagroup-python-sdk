# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from copy import deepcopy
from typing import Any

from datamodel_code_generator.model import pydantic as datamodel_code_generator_pydantic
from datamodel_code_generator.model.pydantic.imports import IMPORT_CONSTR
from datamodel_code_generator.model.pydantic.types import (
    escape_characters,
    string_kwargs,
    transform_kwargs,
)
from datamodel_code_generator.types import DataType, StrictTypes, Types

PYDANTIC_V2_MIGRATION_CONSTRAINTS_MAPPING: dict[str, str] = {"regex": "pattern"}


class PydanticV2DataTypeManager(datamodel_code_generator_pydantic.DataTypeManager):
    r"""
    Custom DataTypeManager to map PydanticV1 types to PydanticV2.

    Notes:
        - This class is a temporary solution until `fastapi-code-generator` bumps up
            its `datamodel-code-generator` from `0.16.1` to `>=0.25.1` which includes
            PydanticV2 support.
            GitHub Issue: https://github.com/koxudaxi/fastapi-code-generator/issues/378
    """

    @staticmethod
    def migrate_datatype_constraints(data_type_kwargs: dict[str, Any]) -> dict[str, Any]:
        """
        Migrates datatype constraints in the given data_type_kwargs dictionary from pydantic v1 to v2 .

        Args:
            data_type_kwargs (dict[str, Any]): A dictionary containing datatype constraints.

        Returns:
            dict[str, Any]: The migrated datatype constraints dictionary.
        """
        migrated_data_type_kwargs: dict[str, Any] = deepcopy(data_type_kwargs)

        for key, value in PYDANTIC_V2_MIGRATION_CONSTRAINTS_MAPPING.items():
            if migrated_data_type_kwargs.get(key):
                migrated_data_type_kwargs.update([(value, migrated_data_type_kwargs.get(key))])
                migrated_data_type_kwargs.pop(key)

        return migrated_data_type_kwargs

    def get_data_str_type(self, types: Types, **kwargs: Any) -> DataType:
        data_type_kwargs: dict[str, Any] = transform_kwargs(kwargs, string_kwargs)
        strict = StrictTypes.str in self.strict_types
        if data_type_kwargs:
            if strict:
                data_type_kwargs["strict"] = True
            if "regex" in data_type_kwargs:
                escaped_regex = data_type_kwargs["regex"].translate(escape_characters)
                data_type_kwargs["regex"] = f"r'{escaped_regex}'"

                # Copied code, single line added.
                data_type_kwargs = PydanticV2DataTypeManager.migrate_datatype_constraints(data_type_kwargs)

            return self.data_type.from_import(IMPORT_CONSTR, kwargs=data_type_kwargs)
        if strict:
            return self.strict_type_map[StrictTypes.str]
        return self.type_map[types]
