import os
import tempfile
from typing import Dict
from .settings import METADATA_TEMPLATE

tempdir = tempfile.gettempdir()
tempfp = os.path.join(tempdir, "percy_metadata_state.json")


class State:
    def __init__(self):
        self.init()

    def init(self) -> State:
        pass

    def exists(self) -> bool:
        pass

    def create_new(self):
        pass

    def read(self) -> Dict[str, object]:
        pass

    def update(self,
               what=str, update: dict) -> Dict[str, object]:
        raise NotImplementedError()
