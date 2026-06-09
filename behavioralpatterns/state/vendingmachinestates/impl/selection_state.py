from ..state import State


class SelectionState(State):
    def __init__(self):
        print("Currently Vending machine is in SelectionState")

    def choose_product(self, machine, code_number):
        # 1. get item of this codeNumber
        item = machine.get_inventory().get_item(code_number)

        # 2. total amount paid by User
        paid_by_user = 0
        for coin in machine.get_coin_list():
            paid_by_user = paid_by_user + coin.value

        # 3. compare product price and amount paid by user
        if paid_by_user < item.get_price():
            print("Insufficient Amount, Product you selected is for price: " + str(item.get_price()) + " and you paid: " + str(paid_by_user))
            self.refund_full_money(machine)
            raise Exception("insufficient amount")
        elif paid_by_user >= item.get_price():
            if paid_by_user > item.get_price():
                self.get_change(paid_by_user - item.get_price())
            from .dispense_state import DispenseState
            machine.set_vending_machine_state(DispenseState(machine, code_number))

    def get_change(self, return_extra_money):
        print("Returned the change in the Coin Dispense Tray: " + str(return_extra_money))
        return return_extra_money

    def refund_full_money(self, machine):
        print("Returned the full amount back in the Coin Dispense Tray")
        from .idle_state import IdleState
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()
