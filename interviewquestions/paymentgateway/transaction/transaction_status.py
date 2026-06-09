from enum import Enum


class TransactionStatus(Enum):
    SUCCESS = "SUCCESS"
    DENIED = "DENIED"
    PENDING = "PENDING"
