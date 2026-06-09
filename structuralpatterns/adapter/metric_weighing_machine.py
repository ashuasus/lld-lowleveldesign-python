from .imperial_weighing_machine_impl import ImperialWeighingMachineImpl
from .weight_machine_adapter_impl import WeightMachineAdapterImpl


# Client - Metric Weighing Machine
def main():
    print("======= Adapter Design Pattern ======")

    # ImperialWeighingMachine - Existing weighing machine is used to weigh the baby in pounds
    weighing_scale_reading = 25.0  # say the baby's weight is 25 pounds
    imperial_weighing_machine = ImperialWeighingMachineImpl(weighing_scale_reading)

    # Adapter to convert to KG
    weight_machine_adapter = WeightMachineAdapterImpl(imperial_weighing_machine)

    # Client gets weight in Kilograms
    print("Weight in KG: " + str(weight_machine_adapter.get_weight_in_kg()))


if __name__ == "__main__":
    main()
