from .Entity.parking_spot import ParkingSpot
from .Entity.vehicle import Vehicle
from .LookupStrategy.random_lookup_strategy import RandomLookupStrategy
from .enums.vehicle_type import VehicleType
from .parkinglot.parking_level import ParkingLevel
from .parkinglot.parking_building import ParkingBuilding
from .parkinglot.parking_lot import ParkingLot
from .parkinglot.entrance_gate import EntranceGate
from .parkinglot.exit_gate import ExitGate
from .payment.cash_payment import CashPayment
from .payment.upi_payment import UPIPayment
from .pricing.cost_computation import CostComputation
from .pricing.fixed_pricing_strategy import FixedPricingStrategy
from .spotManagers.two_wheeler_spot_manager import TwoWheelerSpotManager
from .spotManagers.four_wheeler_spot_manager import FourWheelerSpotManager


def main():
    strategy = RandomLookupStrategy()

    level_one_managers = {}
    level_one_managers[VehicleType.TWO_WHEELER] = TwoWheelerSpotManager(
        [ParkingSpot("L1-S1"), ParkingSpot("L1-S2")], strategy)
    level_one_managers[VehicleType.FOUR_WHEELER] = FourWheelerSpotManager(
        [ParkingSpot("L1-S3")], strategy)

    level1 = ParkingLevel(1, level_one_managers)

    level_two_managers = {}
    level_two_managers[VehicleType.TWO_WHEELER] = TwoWheelerSpotManager(
        [ParkingSpot("L2-S1")], strategy)
    level_two_managers[VehicleType.FOUR_WHEELER] = FourWheelerSpotManager(
        [ParkingSpot("L2-S2"), ParkingSpot("L2-S3")], strategy)

    level2 = ParkingLevel(2, level_two_managers)

    parking_building = ParkingBuilding(
        [level1, level2],
        CostComputation(FixedPricingStrategy())
    )

    parking_lot = ParkingLot(
        parking_building,
        EntranceGate(),
        ExitGate(CostComputation(FixedPricingStrategy()))
    )

    bike = Vehicle("BIKE-101", VehicleType.TWO_WHEELER)
    car = Vehicle("CAR-201", VehicleType.FOUR_WHEELER)

    t1 = parking_lot.vehicle_arrives(bike)
    t2 = parking_lot.vehicle_arrives(car)

    parking_lot.vehicle_exits(t1, CashPayment())
    parking_lot.vehicle_exits(t2, UPIPayment())


if __name__ == "__main__":
    main()
