from interviewquestions.atm.ATMRoomComponents.atm import ATM
from interviewquestions.atm.ATMRoomComponents.user import User
from interviewquestions.atm.ATMRoomComponents.card import Card
from interviewquestions.atm.ATMRoomComponents.user_bank_account import UserBankAccount
from interviewquestions.atm.enums.transaction_type import TransactionType


class ATMRoom:
    def __init__(self):
        self.atm = None
        self.user = None

    def initialize(self):
        self.atm = ATM.get_atm_object()
        self.atm.set_atm_balance(3500, 1, 2, 5)
        self.user = self._create_user()

    def _create_user(self):
        user = User()
        user.set_card(self._create_card())
        return user

    def _create_card(self):
        card = Card()
        card.set_bank_account(self._create_bank_account())
        return card

    def _create_bank_account(self):
        account = UserBankAccount()
        account.set_balance(3000)
        return account


if __name__ == "__main__":
    room = ATMRoom()
    room.initialize()
    room.atm.print_current_atm_status()
    room.atm.get_current_atm_state().insert_card(room.atm, room.user.get_card())
    room.atm.get_current_atm_state().authenticate_pin(room.atm, room.user.get_card(), 112211)
    room.atm.get_current_atm_state().select_operation(room.atm, room.user.get_card(), TransactionType.CASH_WITHDRAWAL)
    room.atm.get_current_atm_state().cash_withdrawal(room.atm, room.user.get_card(), 2700)
    room.atm.print_current_atm_status()
