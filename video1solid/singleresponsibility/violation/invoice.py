from .marker import Marker


# BAD: This class violates SRP by having multiple responsibilities
class Invoice:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity
        self.total = 0

    # Responsibility 1: Calculate the total(business logic)
    def calculate_total(self):
        print("Calculating total...")
        self.total = self.marker.price * self.quantity

    # Responsibility 2: Print the Invoice
    def print_invoice(self):
        # print the Invoice
        print("Printing Invoice...")

    # Responsibility 3: Database Operations
    def save_to_db(self):
        # Save the data into DB
        print("Saving to DB...")
