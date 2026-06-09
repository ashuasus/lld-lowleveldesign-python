from .instrument.instrument_controller import InstrumentController
from .instrument.instrument_do import InstrumentDO
from .instrument.instrument_type import InstrumentType
from .transaction.transaction_controller import TransactionController
from .transaction.transaction_do import TransactionDO
from .user.user_controller import UserController
from .user.user_do import UserDO


def main():
    print("\nLLD Code - Payment Gateway\n")

    instrument_controller = InstrumentController()
    user_controller = UserController()
    transaction_controller = TransactionController()

    # Add USER1
    user1 = UserDO()
    user1.set_name("Alice")
    user1.set_mail("alice@conceptandcoding.com")
    user1_details = user_controller.add_user(user1)

    # Add USER2
    user2 = UserDO()
    user2.set_name("Bob")
    user2.set_mail("bob@conceptandcoding.com")
    user2_details = user_controller.add_user(user2)

    # Add Bank to User1
    bank_instrument_do = InstrumentDO()
    bank_instrument_do.set_bank_account_number("234324234324324")
    bank_instrument_do.set_instrument_type(InstrumentType.BANK)
    bank_instrument_do.set_user_id(user1_details.get_id())
    bank_instrument_do.set_ifsc("ER3223E")
    user1_bank_instrument = instrument_controller.add_instrument(bank_instrument_do)
    print(f"Bank Instrument created for User1: {user1_bank_instrument.get_instrument_id()}")

    # Add Card to User2
    card_instrument_do = InstrumentDO()
    card_instrument_do.set_card_number("1230099")
    card_instrument_do.set_instrument_type(InstrumentType.CARD)
    card_instrument_do.set_cvv_number("0000")
    card_instrument_do.set_user_id(user2_details.get_id())
    user2_card_instrument = instrument_controller.add_instrument(card_instrument_do)
    print(f"Card Instrument created for User2: {user2_card_instrument.get_instrument_id()}")

    # Make Payment
    transaction_do = TransactionDO()
    transaction_do.set_txn_id(101)
    transaction_do.set_amount(500)
    transaction_do.set_sender_id(user1_details.get_id())
    transaction_do.set_receiver_id(user2_details.get_id())
    transaction_do.set_debit_instrument_id(user1_bank_instrument.get_instrument_id())
    transaction_do.set_credit_instrument_id(user2_card_instrument.get_instrument_id())
    transaction_controller.make_payment(transaction_do)

    # Get all instruments of USER1
    user1_instruments = instrument_controller.get_all_instruments(user1_details.get_id())
    for instrument_do in user1_instruments:
        print(f"\nUser1 Name: {user1_details.get_name()}"
              f"; UserID: {instrument_do.get_user_id()}"
              f"; InstrumentID: {instrument_do.get_instrument_id()}"
              f"; InstrumentType: {instrument_do.get_instrument_type().name}")

    # Get all instruments of USER2
    user2_instruments = instrument_controller.get_all_instruments(user2_details.get_id())
    for instrument_do in user2_instruments:
        print(f"User2 Name: {user2_details.get_name()}"
              f"; UserID: {instrument_do.get_user_id()}"
              f"; InstrumentID: {instrument_do.get_instrument_id()}"
              f"; InstrumentType: {instrument_do.get_instrument_type().name}")

    # Get transaction history of USER1
    user1_transaction_list = transaction_controller.get_transaction_history(user1_details.get_id())
    for txn in user1_transaction_list:
        print(f"\nUser1 txnID: {txn.get_txn_id()}"
              f"; Amount: {txn.get_amount()}"
              f"; Sender: {txn.get_sender_id()}"
              f"; Receiver: {txn.get_receiver_id()}")

    # Get transaction history of USER2
    user2_transaction_list = transaction_controller.get_transaction_history(user2_details.get_id())
    for txn in user2_transaction_list:
        print(f"User2 txnID: {txn.get_txn_id()}"
              f"; Amount: {txn.get_amount()}"
              f"; Sender: {txn.get_sender_id()}"
              f"; Receiver: {txn.get_receiver_id()}")


if __name__ == "__main__":
    main()
