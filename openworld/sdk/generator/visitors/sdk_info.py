import configparser
import re
from pathlib import Path
from typing import Dict

from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


# openworld: new visitor.
def get_sdk(parser: OpenAPIParser, model_path: Path) -> Dict[str, object]:
    config = configparser.ConfigParser()
    config.read(f'{Path(__file__).parent}/sdk.config')

    api = config['sdk']['namespace']
    classname = "".join([word.capitalize() for word in re.findall(r'[a-zA-Z]+', api)])
    namespace = classname.lower()
    classname += 'Client'
    version = config['sdk']['version']
    id = f'openworld-sdk-python-{namespace}'
    package = f'openworld.sdk.{namespace}'

    return {
        'api': api,
        'version': version,
        'classname': classname,
        'namespace': namespace,
        'package': package,
        'id': id
    }


visit: Visitor = get_sdk
