from .atm_state import ATMState


class CheckBalanceState(ATMState):
    def __init__(self):
        pass

    def display_balance(self, atm, card):
        print("Your Balance is: " + str(card.get_bank_balance()))
        self.exit(atm)

    def exit(self, atm_object):
        self.return_card()
        from .idle_state import IdleState
        atm_object.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
