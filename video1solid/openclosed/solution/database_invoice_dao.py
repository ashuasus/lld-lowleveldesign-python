from ...singleresponsibility.solution.invoice import Invoice
from .invoice_dao import InvoiceDao


# Concrete implementation for DatabaseInvoiceDao
class DatabaseInvoiceDao(InvoiceDao):
    def __init__(self, invoice):
        # set the invoice
        self.invoice = invoice

    def save(self):
        # Save into the DB the invoice
        print("Saving to DB...")
