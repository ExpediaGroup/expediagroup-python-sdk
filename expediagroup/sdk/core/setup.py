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

from setuptools import setup


def parse_version():
    config_parser = configparser.ConfigParser()
    config_parser.read("./core.config")
    return config_parser["sdk-properties"]["version"]


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="expediagroup-sdk-python-core",
    version=f"{parse_version()}",
    package_data={"config_files": ["core.config"]},
    packages=[
        "expediagroup.sdk.core",
        "expediagroup.sdk.core.configuration",
        "expediagroup.sdk.core.client",
        "expediagroup.sdk.core.constant",
        "expediagroup.sdk.core.model",
        "expediagroup.sdk.core.model.exception",
        "expediagroup.sdk.core.util",
    ],
    package_dir={"expediagroup.sdk.core": "."},
    license="Apache License, Version 2.0",
    author="Expedia Group",
    author_email="oss@expediagroup.com",
    url="https://github.com/ExpediaGroup/expediagroup-sdk-python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=["pydantic", "uri", "requests", "python-dateutil"],
    description="Expedia Group SDK Core Library for Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
)
