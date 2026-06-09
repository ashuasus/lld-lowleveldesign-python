from abc import ABC, abstractmethod


# Step 4: Abstract Factory interface
class CarFactory(ABC):
    # Factory methods
    @abstractmethod
    def create_interior(self):
        pass

    @abstractmethod
    def create_exterior(self):
        pass

    # Template method that uses all factory methods
    def produce_complete_vehicle(self):
        print("Starting complete vehicle production...")

        # Create all components
        interior = self.create_interior()
        exterior = self.create_exterior()

        # Assemble the vehicle
        interior.add_interior_components()
        exterior.add_exterior_components()

        print("Vehicle production completed!")
