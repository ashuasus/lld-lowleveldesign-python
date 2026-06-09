from abc import ABC, abstractmethod
from .product_type import ProductType


class Product(ABC):

    def __init__(self, name: str, price: float, product_type: ProductType):
        self.name = name
        self.original_price = price
        self.type = product_type

    @abstractmethod
    def get_price(self) -> float:
        pass

    def get_type(self) -> ProductType:
        return self.type

    def get_name(self) -> str:
        return self.name
