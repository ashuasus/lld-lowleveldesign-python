from ...singleresponsibility.solution.invoice import Invoice


# Responsibility: Managing Database Operations and File Operations
# BAD: This class violates OCP - needs modification for every new kind of save function
class InvoiceDao:
    def __init__(self, invoice):
        self.invoice = invoice

    def save_to_db(self):
        # Save into the DB the invoice
        print("Saving to DB...")

    # BAD: This design violates OCP
    # Every time we add a new save function, we need to modify existing InvoiceDao class
    def save_to_file(self):
        # Save into the file
        print("Saving to file...")
