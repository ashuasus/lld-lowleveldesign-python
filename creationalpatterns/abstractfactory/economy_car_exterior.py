from .car_exterior import CarExterior


# Step 2: Concrete Products for Economy Car Family
class EconomyCarExterior(CarExterior):
    def add_exterior_components(self):
        print("Adding basic exterior components for Economy Car.")
