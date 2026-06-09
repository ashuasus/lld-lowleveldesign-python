from .instrument import Instrument
from .instrument_type import InstrumentType


class BankInstrument(Instrument):

    def __init__(self, instrument_id: int = 0, user_id: int = 0,
                 instrument_type: InstrumentType = None,
                 bank_account_number: str = None, ifsc_code: str = None):
        super().__init__(instrument_id, user_id, instrument_type)
        self.bank_account_number = bank_account_number
        self.ifsc_code = ifsc_code

    def get_bank_account_number(self) -> str:
        return self.bank_account_number

    def set_bank_account_number(self, bank_account_number: str):
        self.bank_account_number = bank_account_number

    def get_ifsc_code(self) -> str:
        return self.ifsc_code

    def set_ifsc_code(self, ifsc_code: str):
        self.ifsc_code = ifsc_code
