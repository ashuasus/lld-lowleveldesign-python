from .warehouse import Warehouse
from .warehouse_selection_strategy import WarehouseSelectionStrategy


class WarehouseController:

    def __init__(self, warehouse_list: list, warehouse_selection_strategy: WarehouseSelectionStrategy = None):
        self.warehouse_list = warehouse_list
        self.warehouse_selection_strategy = warehouse_selection_strategy

    def add_new_warehouse(self, warehouse: Warehouse):
        self.warehouse_list.append(warehouse)

    def remove_warehouse(self, warehouse: Warehouse):
        self.warehouse_list.remove(warehouse)

    def select_warehouse(self, selection_strategy: WarehouseSelectionStrategy) -> Warehouse:
        self.warehouse_selection_strategy = selection_strategy
        return self.warehouse_selection_strategy.select_warehouse(self.warehouse_list)
