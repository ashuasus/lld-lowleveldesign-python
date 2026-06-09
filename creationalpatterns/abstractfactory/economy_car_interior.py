from .car_interior import CarInterior


# Step 2: Concrete Products for Economy Car Family
class EconomyCarInterior(CarInterior):
    def add_interior_components(self):
        print("Adding basic interior components for Economy Car.")
