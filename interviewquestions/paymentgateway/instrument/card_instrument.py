from .instrument import Instrument
from .instrument_type import InstrumentType


class CardInstrument(Instrument):

    def __init__(self, instrument_id: int = 0, user_id: int = 0,
                 instrument_type: InstrumentType = None,
                 card_number: str = None, cvv: str = None):
        super().__init__(instrument_id, user_id, instrument_type)
        self.card_number = card_number
        self.cvv = cvv

    def get_card_number(self) -> str:
        return self.card_number

    def set_card_number(self, card_number: str):
        self.card_number = card_number

    def get_cvv(self) -> str:
        return self.cvv

    def set_cvv(self, cvv: str):
        self.cvv = cvv
