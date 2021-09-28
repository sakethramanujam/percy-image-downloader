import json
import os
import tempfile
from typing import Dict

from .settings import METADATA_TEMPLATE

TEMPDIR = tempfile.gettempdir()
STATE_PATH = os.path.join(TEMPDIR, "percy_metadata_state.json")


class State:
    def __init__(self):
        self.path = STATE_PATH

    def _exists(self) -> bool:
        if not os.path.isfile(self.path):
            return False
        return True

    def _create(self):
        with open(path, "w") as f:
            f.write(json.dumps(METADATA_TEMPLATE))

    def read(self) -> Dict[str, object]:
        pass

    def update(self,
               what: str,
               update: dict) -> Dict[str, object]:
        raise NotImplementedError()
