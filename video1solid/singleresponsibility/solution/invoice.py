from .marker import Marker


# GOOD: Following SRP - Each class has a single responsibility

# Responsibility: Managing Invoice data only
class Invoice:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity
        self.total = 0

    # Responsibility 1: Calculate the total(business logic)
    def calculate_total(self):
        print("Calculating total...")
        self.total = self.marker.price * self.quantity
