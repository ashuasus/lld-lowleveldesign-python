from .invoice import Invoice


# Responsibility 2: Managing Database Operations only
class InvoiceDao:
    def __init__(self, invoice):
        self.invoice = invoice

    def save_to_db(self):
        # Save into the DB the invoice
        print("Saving to DB...")
