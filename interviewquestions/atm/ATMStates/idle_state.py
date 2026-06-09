from .atm_state import ATMState


class IdleState(ATMState):
    def insert_card(self, atm, card):
        print("Card is inserted")
        from .has_card_state import HasCardState
        atm.set_current_atm_state(HasCardState())
