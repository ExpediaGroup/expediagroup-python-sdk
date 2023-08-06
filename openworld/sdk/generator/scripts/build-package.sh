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
  echo "Usage: >> ./generate_models.sh -n namespace"
  exit 1
}

function validate_arguments() {
  if [ -z "$namespace" ]
  then
    fail
  fi
}

namespace=''

# Parse arguments
while getopts ":n:v:i:" OPTION; do
        case $OPTION in
              n) namespace="$OPTARG";;
              ?) echo "Invalid options!";;
        esac
done; validate_arguments

normalized_namespace=$(echo "$namespace"|gsed -e 's/\(.*\)/\L\1/')
normalized_namespace=$(echo "$normalized_namespace"|gsed -e 's/[^a-zA-Z0-9]//g')

cd .. &&\
go install github.com/google/addlicense@latest &&\
`go env GOPATH`/bin/addlicense -f ../../LICENSE_header.txt . &&\
cd - &&\
mkdir -p "package/openworld/sdk/$normalized_namespace" &&\
cp -a "client/sdk/." "package/openworld/sdk/$normalized_namespace/" &&\
mv "package/openworld/sdk/$normalized_namespace/__model__.py" "package/openworld/sdk/$normalized_namespace/model.py" &&\
cp "resources/requirements.txt" "package/requirements.txt" &&\
mv "package/openworld/sdk/$normalized_namespace/setup.py" "package/setup.py" &&\
rm -rf "package/openworld/sdk/$normalized_namespace/models.py" &&\
cd package &&\
python3 -m build
