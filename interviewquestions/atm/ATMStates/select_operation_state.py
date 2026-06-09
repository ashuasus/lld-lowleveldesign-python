from .atm_state import ATMState
from ..enums.transaction_type import TransactionType


class SelectOperationState(ATMState):
    def __init__(self):
        self._show_operations()

    def select_operation(self, atm_object, card, txn_type):
        if txn_type == TransactionType.CASH_WITHDRAWAL:
            from .cash_withdrawal_state import CashWithdrawalState
            atm_object.set_current_atm_state(CashWithdrawalState())
        elif txn_type == TransactionType.BALANCE_CHECK:
            from .check_balance_state import CheckBalanceState
            atm_object.set_current_atm_state(CheckBalanceState())
        else:
            print("Invalid Option")
            self.exit(atm_object)

    def exit(self, atm_object):
        self.return_card()
        from .idle_state import IdleState
        atm_object.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")

    def _show_operations(self):
        print("Please select the Operation")
        TransactionType.show_all_transaction_types()
