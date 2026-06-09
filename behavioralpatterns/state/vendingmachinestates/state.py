class State:
    def click_on_insert_coin_button(self, machine):
        pass  # by default nothing happens

    def click_on_start_product_selection_button(self, machine):
        pass  # by default nothing happens

    def insert_coin(self, machine, coin):
        pass  # by default nothing happens

    def choose_product(self, machine, code_number):
        pass  # by default nothing happens

    def get_change(self, return_change_money):
        return 0  # by default nothing happens

    def dispense_product(self, machine, code_number):
        return None  # by default nothing happens

    def refund_full_money(self, machine):
        return None  # by default nothing happens

    def update_inventory(self, machine, item, code_number):
        pass  # by default nothing happens
