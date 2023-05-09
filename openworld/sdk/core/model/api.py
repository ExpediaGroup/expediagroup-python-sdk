from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class Response:
    raw: requests.Response
    body: Any
