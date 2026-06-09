import random
from .instrument_service import InstrumentService
from .instrument_do import InstrumentDO
from .bank_instrument import BankInstrument
from .instrument_type import InstrumentType


class BankService(InstrumentService):

    def __init__(self):
        super().__init__()

    def add_instrument(self, instrument_do: InstrumentDO) -> InstrumentDO:
        # bank specific logic here
        bank_instrument = BankInstrument()
        bank_instrument.instrument_id = random.randint(10, 99)
        bank_instrument.bank_account_number = instrument_do.bank_account_number
        bank_instrument.ifsc_code = instrument_do.ifsc
        bank_instrument.instrument_type = InstrumentType.BANK
        bank_instrument.user_id = instrument_do.user_id

        user_instruments_list = InstrumentService.user_vs_instruments.get(bank_instrument.user_id)
        if user_instruments_list is None:
            user_instruments_list = []
            InstrumentService.user_vs_instruments[bank_instrument.user_id] = user_instruments_list
        user_instruments_list.append(bank_instrument)
        return self._map_bank_instrument_to_instrument_do(bank_instrument)

    def get_instruments_by_user_id(self, user_id: int) -> list:
        user_instruments = InstrumentService.user_vs_instruments.get(user_id, [])
        user_instruments_fetched = []
        for instrument in user_instruments:
            if instrument.get_instrument_type() == InstrumentType.BANK:
                user_instruments_fetched.append(
                    self._map_bank_instrument_to_instrument_do(instrument)
                )
        return user_instruments_fetched

    def _map_bank_instrument_to_instrument_do(self, bank_instrument: BankInstrument) -> InstrumentDO:
        instrument_do_obj = InstrumentDO()
        instrument_do_obj.instrument_type = bank_instrument.instrument_type
        instrument_do_obj.instrument_id = bank_instrument.instrument_id
        instrument_do_obj.bank_account_number = bank_instrument.bank_account_number
        instrument_do_obj.ifsc = bank_instrument.ifsc_code
        instrument_do_obj.user_id = bank_instrument.user_id
        return instrument_do_obj
