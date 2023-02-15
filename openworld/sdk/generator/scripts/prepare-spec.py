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

from base64 import b64decode
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
from typer import run, Option


def decode_base64_spec_file(encoded_file_content: str):
    decoded_file_content = b64decode(encoded_file_content)
    return decoded_file_content


def unzip_base64_encoded_zip_file(base64_zip_file_content: str):
    decoded_zip_file_content = BytesIO(b64decode(base64_zip_file_content))
    zip_file = ZipFile(decoded_zip_file_content)

    specs_path = Path('specs')
    zip_file.extractall(path=specs_path)

    for spec in specs_path.glob('*.yaml'):
        spec.rename(f'{specs_path.absolute()}/spec.yaml')


def main(spec: str = Option(..., "--input", "-i")):
    unzip_base64_encoded_zip_file(spec)


if __name__ == '__main__':
    run(main)
