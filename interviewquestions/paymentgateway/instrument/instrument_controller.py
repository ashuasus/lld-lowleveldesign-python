from .instrument_do import InstrumentDO
from .instrument_service_factory import InstrumentServiceFactory
from .instrument_type import InstrumentType


class InstrumentController:

    def __init__(self):
        self.instrument_controller_factory = InstrumentServiceFactory()

    def add_instrument(self, instrument: InstrumentDO) -> InstrumentDO:
        instrument_controller = self.instrument_controller_factory.get_instrument_service(
            instrument.instrument_type
        )
        return instrument_controller.add_instrument(instrument)

    def get_all_instruments(self, user_id: int) -> list:
        bank_instrument_controller = self.instrument_controller_factory.get_instrument_service(
            InstrumentType.BANK
        )
        card_instrument_controller = self.instrument_controller_factory.get_instrument_service(
            InstrumentType.CARD
        )
        instrument_do_list = bank_instrument_controller.get_instruments_by_user_id(user_id)
        instrument_do_list.extend(card_instrument_controller.get_instruments_by_user_id(user_id))
        return instrument_do_list

    def get_instrument_by_id(self, user_id: int, instrument_id: int) -> InstrumentDO:
        instrument_do_list = self.get_all_instruments(user_id)

        for instrument_do in instrument_do_list:
            if instrument_do.get_instrument_id() == instrument_id:
                return instrument_do
        return None
