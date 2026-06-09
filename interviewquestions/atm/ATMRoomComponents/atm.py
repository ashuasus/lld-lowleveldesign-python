from interviewquestions.atm.ATMStates.idle_state import IdleState


class ATM:
    _atm_object = None

    def __new__(cls):
        if cls._atm_object is None:
            cls._atm_object = super().__new__(cls)
            cls._atm_object.current_atm_state = None
            cls._atm_object.no_of_two_thousand_notes = 0
            cls._atm_object.no_of_five_hundred_notes = 0
            cls._atm_object.no_of_one_hundred_notes = 0
            cls._atm_object._atm_balance = 0
        return cls._atm_object

    @classmethod
    def get_atm_object(cls):
        obj = cls()
        obj.set_current_atm_state(IdleState())
        return obj

    def get_current_atm_state(self):
        return self.current_atm_state

    def set_current_atm_state(self, state):
        self.current_atm_state = state

    def get_atm_balance(self):
        return self._atm_balance

    def set_atm_balance(self, balance, two_k, five_hundred, one_hundred):
        self._atm_balance = balance
        self.no_of_two_thousand_notes = two_k
        self.no_of_five_hundred_notes = five_hundred
        self.no_of_one_hundred_notes = one_hundred

    def get_no_of_two_thousand_notes(self):
        return self.no_of_two_thousand_notes

    def get_no_of_five_hundred_notes(self):
        return self.no_of_five_hundred_notes

    def get_no_of_one_hundred_notes(self):
        return self.no_of_one_hundred_notes

    def deduct_atm_balance(self, amount):
        self._atm_balance -= amount

    def deduct_two_thousand_notes(self, number):
        self.no_of_two_thousand_notes -= number

    def deduct_five_hundred_notes(self, number):
        self.no_of_five_hundred_notes -= number

    def deduct_one_hundred_notes(self, number):
        self.no_of_one_hundred_notes -= number

    def print_current_atm_status(self):
        print(f"Balance: {self._atm_balance}")
        print(f"2kNotes: {self.no_of_two_thousand_notes}")
        print(f"500Notes: {self.no_of_five_hundred_notes}")
        print(f"100Notes: {self.no_of_one_hundred_notes}")
