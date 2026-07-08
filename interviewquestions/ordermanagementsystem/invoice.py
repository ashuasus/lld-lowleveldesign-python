class Invoice:

    def __init__(self):
        self.total_item_price = 0
        self.total_tax = 0
        self.total_final_price = 0

    def generate_invoice(self, order):
        # computes totals from order; hardcoded for demo
        self.total_item_price = 200
        self.total_tax = 20
        self.total_final_price = 220
        print(f"Invoice generated: item={self.total_item_price}, "
              f"tax={self.total_tax}, total={self.total_final_price}")
