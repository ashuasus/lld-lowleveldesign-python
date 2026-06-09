from ..state import State


class DispenseState(State):
    def __init__(self, machine, code_number):
        print("Currently Vending machine is in DispenseState")
        self.dispense_product(machine, code_number)

    def dispense_product(self, machine, code_number):
        print("Product has been dispensed")
        item = machine.get_inventory().get_item(code_number)
        machine.get_inventory().update_sold_out_item(code_number)
        from .idle_state import IdleState
        machine.set_vending_machine_state(IdleState(machine))
        return item
