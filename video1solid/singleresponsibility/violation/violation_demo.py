from .marker import Marker
from .invoice import Invoice


# Usage example
def main():
    invoice = Invoice(Marker("name", "color", 10, 2020), 10)
    invoice.calculate_total()
    invoice.save_to_db()
    invoice.print_invoice()


if __name__ == "__main__":
    main()
