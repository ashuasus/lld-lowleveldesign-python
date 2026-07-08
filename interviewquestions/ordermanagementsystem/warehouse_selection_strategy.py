from abc import ABC, abstractmethod


class WarehouseSelectionStrategy(ABC):

    @abstractmethod
    def select_warehouse(self, warehouse_list: list):
        pass
