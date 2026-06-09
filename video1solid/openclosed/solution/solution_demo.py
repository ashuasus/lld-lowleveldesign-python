from ...singleresponsibility.solution.invoice import Invoice
from ...singleresponsibility.solution.marker import Marker
from .database_invoice_dao import DatabaseInvoiceDao
from .file_invoice_dao import FileInvoiceDao


# Usage demonstrating OCP compliance
def main():
    invoice = Invoice(Marker("name", "color", 10, 2020), 10)
    invoice.calculate_total()

    database_invoice_dao = DatabaseInvoiceDao(invoice)
    database_invoice_dao.save()

    file_invoice_dao = FileInvoiceDao(invoice)
    file_invoice_dao.save()

    # The system is:
    # - OPEN for extension (new save functions can be added)
    # - CLOSED for modification (existing code remains unchanged)


if __name__ == "__main__":
    main()
