import json

from .dataclass_json_encoder import DataclassJSONEncoder


class JSONDataclass:
    def json_stringify(self) -> str:
        return json.dumps(self, cls=DataclassJSONEncoder)
