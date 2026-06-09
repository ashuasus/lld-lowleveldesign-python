from abc import ABC
from .instrument_type import InstrumentType


class Instrument(ABC):

    def __init__(self, instrument_id: int = 0, user_id: int = 0, instrument_type: InstrumentType = None):
        self.instrument_id = instrument_id
        self.user_id = user_id
        self.instrument_type = instrument_type

    def get_instrument_id(self) -> int:
        return self.instrument_id

    def set_instrument_id(self, instrument_id: int):
        self.instrument_id = instrument_id

    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, user_id: int):
        self.user_id = user_id

    def get_instrument_type(self) -> InstrumentType:
        return self.instrument_type

    def set_instrument_type(self, instrument_type: InstrumentType):
        self.instrument_type = instrument_type
