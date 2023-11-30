import json
from typing import Any

from pydantic import BaseModel, Field


class RequestHeaders(BaseModel):
    headers: Any = Field(default=None)

    def unwrap(self) -> dict[str, Any]:
        if not self.headers:
            return dict()

        return json.loads(self.model_dump_json()).get("headers")
