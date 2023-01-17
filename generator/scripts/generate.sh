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
  echo "Usage: >> ./generate.sh -i input_spec_file -n namespace -v version"
  exit 1
}

function validate_arguments() {
  if [ -z "$sdk_namespace" ]
  then
    fail
  fi

  if [ -z "$sdk_version" ]
  then
    fail
  fi

  if [ -z "$input_spec" ]
  then
    fail
  fi
}

sdk_namespace=''
sdk_version=''
input_spec=''

# Parse arguments
while getopts ":n:v:i:" OPTION; do
        case $OPTION in
              n) sdk_namespace="$OPTARG";;
              v) sdk_version="$OPTARG";;
              i) input_spec="$OPTARG";;
              ?) echo "Invalid options!";;
        esac
done; validate_arguments

normalized_namespace=$(echo "$sdk_namespace"|sed -e 's/\(.*\)/\L\1/')
normalized_namespace=$(echo "$normalized_namespace"|sed -e 's/[^a-z0-9]//g')

wrong_import="from openworld/sdk/$normalized_namespace"
new_import="from openworld.sdk.$normalized_namespace"

# Generates an SDK wheel
echo "Generating an SDK"\
&& cd ../openapi/module || exit \
&& mvn clean install \
&& cd ..\
&& mvn clean install \
&& mvn exec:java "-Dnamespace=$sdk_namespace" -DsdkVersion=$sdk_version "-Dspec=$input_spec"\
&& cd ..\
&& rm -rf ./package\
&& mkdir -p package/openworld/sdk/$normalized_namespace/client\
&& mkdir package/openworld/sdk/$normalized_namespace/model\
&& mv ./openapi/target/sdk/openworld/sdk/$normalized_namespace/client/tags/*.py ./package/openworld/sdk/$normalized_namespace/client/\
&& mv ./openapi/target/sdk/openworld/sdk/$normalized_namespace/model/*.py ./package/openworld/sdk/$normalized_namespace/model/\
&& mv ./openapi/target/sdk/requirements.txt ./package/requirements.txt\
&& mv ./openapi/target/sdk/setup.py ./package/setup.py\
\
\
&& echo "Adding Imports"\
&& cd ./scripts || exit \
&& cd ../package/openworld/sdk/"$normalized_namespace"/model\
&& python3 ./../../../../../scripts/add-imports.py . \
&& pip3 install autoflake\
&& autoflake --in-place --remove-all-unused-imports -r .\
&& cd ../client\
&& sed -i "s@$wrong_import@$new_import@" ./* \
&& python3 ./../../../../../scripts/add-imports.py . \
&& autoflake --in-place --remove-all-unused-imports -r .\
&& cd ../../../..\
&& `go env GOPATH`/bin/addlicense -f ../../LICENSE_header.txt . \
\
\
&& echo "Building a Wheel"\
&& pip3 install build \
&& pip3 install virtualenv \
&& python3 -m build\
&& mkdir -p ../wheels\
&& mv ./dist/* ../wheels/\
\
\
&& echo "Done"
