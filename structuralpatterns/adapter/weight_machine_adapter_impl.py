from .weighing_machine_adapter import WeighingMachineAdapter


# Concrete Adapter converts pounds → kg
class WeightMachineAdapterImpl(WeighingMachineAdapter):
    def __init__(self, weight_machine_in_pounds):
        # Adaptee Reference
        self.imperial_weighing_machine = weight_machine_in_pounds

    def get_weight_in_kg(self):
        weight_in_pound = self.imperial_weighing_machine.get_weight_in_pounds()
        # Conversion formula: 1 pound = 0.453592 kg
        return weight_in_pound * 0.45
