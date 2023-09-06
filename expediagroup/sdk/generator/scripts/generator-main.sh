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
  echo "Usage: >> ./generator-main.sh -i input_spec_file -n namespace -v version"
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

cp $input_spec ./client/spec.yaml
pip3 install -r ../../../requirements-dev.txt &&\
scripts/generate-sdk.sh -i "spec.yaml" -v "$sdk_version" -n "$sdk_namespace" &&\
scripts/build-package.sh -n "$sdk_namespace"
