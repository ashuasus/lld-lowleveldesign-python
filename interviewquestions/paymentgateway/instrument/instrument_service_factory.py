from .instrument_service import InstrumentService
from .instrument_type import InstrumentType
from .bank_service import BankService
from .card_service import CardService


class InstrumentServiceFactory:

    def get_instrument_service(self, instrument_type: InstrumentType) -> InstrumentService:
        if instrument_type == InstrumentType.BANK:
            return BankService()
        elif instrument_type == InstrumentType.CARD:
            return CardService()
        return None
