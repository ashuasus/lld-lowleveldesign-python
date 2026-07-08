from enum import Enum


class OrderStatus(Enum):
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    RETURNED = "RETURNED"
    UNDELIVERED = "UNDELIVERED"
