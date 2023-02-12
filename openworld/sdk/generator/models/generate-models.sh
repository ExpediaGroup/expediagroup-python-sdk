#!/bin/bash
#!/bin/bash

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


function fail {
  echo "SDK properties can't be empty!"
  echo "Usage: >> ./generate_models.sh -i input_spec_file"
  exit 1
}

function validate_arguments() {
  if [ -z "$input_spec" ]
  then
    fail
  fi
}

input_spec=''

# Parse arguments
while getopts ":n:v:i:" OPTION; do
        case $OPTION in
              i) input_spec="$OPTARG";;
              ?) echo "Invalid options!";;
        esac
done; validate_arguments

# Generate SDK Models
datamodel-codegen --input-file-type openapi --input $input_spec --use-schema-description  --use-standard-collections --output ./models.py --collapse-root-models --custom-template-dir ./templates --use-field-description
