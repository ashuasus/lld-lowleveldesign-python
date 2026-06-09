from ...singleresponsibility.solution.invoice import Invoice
from .invoice_dao import InvoiceDao


# Concrete implementation for FileInvoiceDao
# NEW File Save Operation: An extension without modification!
class FileInvoiceDao(InvoiceDao):
    def __init__(self, invoice):
        # set the invoice
        self.invoice = invoice

    def save(self):
        # Save into the file the invoice
        print("Saving to file...")
