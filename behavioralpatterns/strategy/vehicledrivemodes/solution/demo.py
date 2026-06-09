from .context.sports_vehicle import SportsVehicle
from .context.goods_vehicle import GoodsVehicle
from .context.hybrid_vehicle import HybridVehicle
from .strategies.sports_drive import SportsDrive
from .strategies.normal_drive import NormalDrive
from .strategies.ev_drive import EVDrive


def main():
    print("###### Strategy Design Pattern ######")
    print("###### Example: Vehicle Drive Modes ######")

    vehicle = SportsVehicle(SportsDrive())
    vehicle.drive()

    vehicle = GoodsVehicle(NormalDrive())
    vehicle.drive()

    vehicle = HybridVehicle(EVDrive())
    vehicle.drive()

    vehicle = GoodsVehicle(NormalDrive())
    vehicle.drive()


if __name__ == "__main__":
    main()
