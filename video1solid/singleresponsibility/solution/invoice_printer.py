from .invoice import Invoice


# Responsibility 3: Printing the Invoice only
class InvoicePrinter:
    def __init__(self, invoice):
        self.invoice = invoice

    def print(self):
        # print the invoice
        print("Printing Invoice...")
