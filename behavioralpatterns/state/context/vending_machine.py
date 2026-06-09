from .inventory import Inventory


class VendingMachine:
    def __init__(self):
        from ..vendingmachinestates.impl.idle_state import IdleState
        self._vending_machine_state = IdleState()
        self._inventory = Inventory(10)
        self._coin_list = []

    def get_vending_machine_state(self):
        return self._vending_machine_state

    def set_vending_machine_state(self, state):
        self._vending_machine_state = state

    def get_inventory(self):
        return self._inventory

    def set_inventory(self, inventory):
        self._inventory = inventory

    def get_coin_list(self):
        return self._coin_list

    def set_coin_list(self, coin_list):
        self._coin_list = coin_list
