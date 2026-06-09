from ..instrument.instrument_controller import InstrumentController
from .transaction import Transaction
from .transaction_do import TransactionDO
from .transaction_status import TransactionStatus
from .processor import Processor


class TransactionService:

    user_vs_transactions_list: dict = {}  # static: shared across all instances

    def __init__(self):
        self.instrument_controller = InstrumentController()
        self.processor = Processor()

    def get_transaction_history(self, user_id: int) -> list:
        return TransactionService.user_vs_transactions_list.get(user_id)

    def make_payment(self, txn_do: TransactionDO) -> TransactionDO:
        # validate details

        # load sender instrument details which need to be passed to processors
        sender_instrument_do = self.instrument_controller.get_instrument_by_id(
            txn_do.get_sender_id(), txn_do.get_debit_instrument_id()
        )

        # load receiver instrument details which need to be passed to processors
        receiver_instrument_do = self.instrument_controller.get_instrument_by_id(
            txn_do.get_receiver_id(), txn_do.get_credit_instrument_id()
        )

        # pass the instrument details to processor
        self.processor.process_payment(sender_instrument_do, receiver_instrument_do)

        # based on processor response, we will set the status. for now hard coding it to SUCCESS
        txn = Transaction()
        txn.set_amount(txn_do.get_amount())
        txn.set_txn_id(txn_do.get_txn_id())
        txn.set_sender_id(txn_do.get_sender_id())
        txn.set_receiver_id(txn_do.get_receiver_id())
        txn.set_debit_instrument_id(txn_do.get_debit_instrument_id())
        txn.set_credit_instrument_id(txn_do.get_credit_instrument_id())
        txn.set_status(TransactionStatus.SUCCESS)

        # history
        sender_txns_list = TransactionService.user_vs_transactions_list.get(txn.get_sender_id())
        if sender_txns_list is None:
            sender_txns_list = []
            TransactionService.user_vs_transactions_list[txn.get_sender_id()] = sender_txns_list
        sender_txns_list.append(txn)

        receiver_txn_list = TransactionService.user_vs_transactions_list.get(txn.get_receiver_id())
        if receiver_txn_list is None:
            receiver_txn_list = []
            TransactionService.user_vs_transactions_list[txn.get_receiver_id()] = receiver_txn_list
        receiver_txn_list.append(txn)

        txn_do.set_txn_id(txn.get_txn_id())
        txn_do.set_status(txn.get_status())
        return txn_do
