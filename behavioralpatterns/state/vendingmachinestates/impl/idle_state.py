from ..state import State


class IdleState(State):
    def __init__(self, machine=None):
        print("Currently Vending machine is in IdleState")
        if machine is not None:
            machine.set_coin_list([])

    def click_on_insert_coin_button(self, machine):
        from .has_money_state import HasMoneyState
        machine.set_vending_machine_state(HasMoneyState())

    def update_inventory(self, machine, item, code_number):
        machine.get_inventory().add_item(item, code_number)
