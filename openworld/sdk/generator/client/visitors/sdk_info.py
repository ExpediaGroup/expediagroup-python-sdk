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


import configparser
import re
from pathlib import Path

from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


# openworld: new visitor.
def get_sdk(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    config = configparser.ConfigParser()
    config.read(f"{Path(__file__).parent}/sdk.config")

    api = config["sdk"]["namespace"]
    classname = "".join([word.capitalize() for word in re.findall(r"[a-zA-Z]+", api)])
    namespace = classname.lower()
    classname += "Client"
    version = config["sdk"]["version"]
    id = f"openworld-sdk-python-{namespace}"
    package = f"openworld.sdk.{namespace}"

    return {"api": api, "version": version, "classname": classname, "namespace": namespace, "package": package, "id": id}


visit: Visitor = get_sdk
