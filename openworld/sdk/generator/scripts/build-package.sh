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

normalized_namespace=$(echo "$namespace"|sed -e 's/\(.*\)/\L\1/')
normalized_namespace=$(echo "$normalized_namespace"|sed -e 's/[^a-z0-9]//g')

mkdir -p "package/openworld/sdk/$normalized_namespace" &&\
cp -a "client/sdk/." "package/openworld/sdk/$normalized_namespace/" &&\
cp "models/models.py" "package/openworld/sdk/$normalized_namespace/models.py" &&\
cp "resources/requirements.txt" "package/requirements.txt" &&\
mv "package/openworld/sdk/$normalized_namespace/setup.py" "package/setup.py" &&\
cd package &&\
python3 -m build
