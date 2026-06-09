from ...singleresponsibility.solution.invoice import Invoice
from ...singleresponsibility.solution.marker import Marker
from .invoice_dao import InvoiceDao


# Usage example - showing the problem
def main():
    invoice = Invoice(Marker("name", "color", 10, 2020), 10)
    invoice.calculate_total()

    database_file_save = InvoiceDao(invoice)
    database_file_save.save_to_db()
    database_file_save.save_to_file()

    # Problem: If we want to add a new function like save_to_mongodb(),
    # we need to modify InvoiceDao and all its derived classes(if exists)
    # This violates the "closed for modification" part of OCP


if __name__ == "__main__":
    main()
