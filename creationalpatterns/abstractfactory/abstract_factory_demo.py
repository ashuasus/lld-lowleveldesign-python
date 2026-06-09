from .car_factory_provider import CarFactoryProvider, CarType


# Step 7: Client Application
def main():
    print("=====Abstract Factory Design Pattern=====")

    # Get Factory Provider
    car_factory_provider = CarFactoryProvider()

    # Get Economy Car Factory
    economy_car = car_factory_provider.get_factory(CarType.ECONOMY, "Honda")
    economy_car.produce_complete_vehicle()

    # Get Luxury Car Factory
    luxury_car = car_factory_provider.get_factory(CarType.LUXURY, "Mercedes")
    luxury_car.produce_complete_vehicle()

    # Get Premium Car Factory
    premium_car = car_factory_provider.get_factory(CarType.PREMIUM, "Rolls Royce")
    premium_car.produce_complete_vehicle()


if __name__ == "__main__":
    main()
