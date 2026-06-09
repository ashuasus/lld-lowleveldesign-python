from abc import ABC, abstractmethod
from .instrument_do import InstrumentDO


class InstrumentService(ABC):

    user_vs_instruments: dict = {}  # static: shared across all instances

    @abstractmethod
    def add_instrument(self, instrument_do: InstrumentDO) -> InstrumentDO:
        pass

    @abstractmethod
    def get_instruments_by_user_id(self, user_id: int) -> list:
        pass
