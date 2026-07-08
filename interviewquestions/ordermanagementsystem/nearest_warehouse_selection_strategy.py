from .warehouse_selection_strategy import WarehouseSelectionStrategy


class NearestWarehouseSelectionStrategy(WarehouseSelectionStrategy):

    def select_warehouse(self, warehouse_list: list):
        # algo to pick nearest warehouse; picking first for demo
        return warehouse_list[0]
