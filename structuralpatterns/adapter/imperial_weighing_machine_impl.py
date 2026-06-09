from .imperial_weighing_machine import ImperialWeighingMachine


# Adaptee - Existing Incompatible class
class ImperialWeighingMachineImpl(ImperialWeighingMachine):
    def __init__(self, weighing_scale_reading):
        self.weight_in_pounds = weighing_scale_reading

    # Third-party weighing machine (US model) – returns pounds
    def get_weight_in_pounds(self):
        return self.weight_in_pounds
