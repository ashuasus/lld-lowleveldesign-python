from ..state import State


class HasMoneyState(State):
    def __init__(self):
        print("Currently Vending machine is in HasMoneyState")

    def click_on_start_product_selection_button(self, machine):
        from .selection_state import SelectionState
        machine.set_vending_machine_state(SelectionState())

    def insert_coin(self, machine, coin):
        print("Accepted the coin")
        machine.get_coin_list().append(coin)

    def refund_full_money(self, machine):
        print("Returned the full amount back in the Coin Dispense Tray")
        from .idle_state import IdleState
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()
