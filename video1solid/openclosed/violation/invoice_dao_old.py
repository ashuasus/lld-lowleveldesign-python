from ...singleresponsibility.solution.invoice import Invoice


# Responsibility: Managing Database Operations only
class InvoiceDaoOld:
    def __init__(self, invoice):
        self.invoice = invoice

    def save_to_db(self):
        # Save into the DB the invoice
        print("Saving to DB...")
