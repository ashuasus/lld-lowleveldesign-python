from .marker import Marker
from .invoice import Invoice
from .invoice_dao import InvoiceDao
from .invoice_printer import InvoicePrinter


# Usage example showing how all classes work together
def main():
    # create the service objects
    invoice = Invoice(Marker("name", "color", 10, 2020), 10)
    invoice_dao = InvoiceDao(invoice)
    invoice_printer = InvoicePrinter(invoice)

    # use the services
    invoice.calculate_total()
    invoice_dao.save_to_db()
    invoice_printer.print()


if __name__ == "__main__":
    main()
