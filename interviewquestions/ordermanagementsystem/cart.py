class Cart:

    def __init__(self):
        self.product_category_id_vs_count = {}

    def add_item(self, product_category_id: int, count: int):
        if product_category_id in self.product_category_id_vs_count:
            self.product_category_id_vs_count[product_category_id] += count
        else:
            self.product_category_id_vs_count[product_category_id] = count

    def remove_item(self, product_category_id: int, count: int):
        if product_category_id in self.product_category_id_vs_count:
            current = self.product_category_id_vs_count[product_category_id]
            if current - count <= 0:
                del self.product_category_id_vs_count[product_category_id]
            else:
                self.product_category_id_vs_count[product_category_id] = current - count

    def empty_cart(self):
        self.product_category_id_vs_count = {}

    def get_cart_items(self) -> dict:
        return self.product_category_id_vs_count
