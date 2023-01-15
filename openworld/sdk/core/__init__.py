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

import logging
from logging.config import fileConfig

try:
    with open(file="logging.cfg", mode="r+") as f:
        fileConfig(f)
except FileNotFoundError:
    default_logger_handler = logging.StreamHandler()
    default_formatter = logging.Formatter(
        fmt="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    default_logger_handler.setFormatter(default_formatter)

    default_logger = logging.getLogger(name="openworld")
    default_logger.addHandler(default_logger_handler)
    default_logger.setLevel(level=logging.DEBUG)
