import random
from .instrument_service import InstrumentService
from .instrument_do import InstrumentDO
from .card_instrument import CardInstrument
from .instrument_type import InstrumentType


class CardService(InstrumentService):

    def __init__(self):
        super().__init__()

    def add_instrument(self, instrument_do: InstrumentDO) -> InstrumentDO:
        # card specific logic here
        card_instrument = CardInstrument()
        card_instrument.instrument_id = random.randint(10, 99)
        card_instrument.card_number = instrument_do.card_number
        card_instrument.cvv = instrument_do.cvv_number
        card_instrument.instrument_type = InstrumentType.CARD
        card_instrument.user_id = instrument_do.user_id

        user_instruments_list = InstrumentService.user_vs_instruments.get(card_instrument.user_id)
        if user_instruments_list is None:
            user_instruments_list = []
            InstrumentService.user_vs_instruments[card_instrument.user_id] = user_instruments_list
        user_instruments_list.append(card_instrument)
        return self._map_card_instrument_to_instrument_do(card_instrument)

    def _map_card_instrument_to_instrument_do(self, card_instrument: CardInstrument) -> InstrumentDO:
        instrument_do_obj = InstrumentDO()
        instrument_do_obj.instrument_type = card_instrument.instrument_type
        instrument_do_obj.instrument_id = card_instrument.instrument_id
        instrument_do_obj.card_number = card_instrument.card_number
        instrument_do_obj.cvv_number = card_instrument.cvv
        instrument_do_obj.user_id = card_instrument.user_id
        return instrument_do_obj

    def get_instruments_by_user_id(self, user_id: int) -> list:
        user_instruments = InstrumentService.user_vs_instruments.get(user_id, [])
        user_instruments_fetched = []
        for instrument in user_instruments:
            if instrument.get_instrument_type() == InstrumentType.CARD:
                user_instruments_fetched.append(
                    self._map_card_instrument_to_instrument_do(instrument)
                )
        return user_instruments_fetched
