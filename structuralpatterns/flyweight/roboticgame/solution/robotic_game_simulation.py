from .robotic_factory import RoboticFactory


# Client – supplies extrinsic state when using flyweights
def main():
    print("====== Flyweight Design Pattern ======")
    # Factory pattern is used to create objects
    # Flyweight pattern is used to reuse objects

    # Create 2 Humanoid robots and provide display coordinates(extrinsic state) at runtime
    humanoid_robot1 = RoboticFactory.create_robot("HUMANOID")
    humanoid_robot1.display(1, 2)
    humanoid_robot2 = RoboticFactory.create_robot("HUMANOID")
    humanoid_robot2.display(10, 30)

    # Create 2 Robotic Dog robots and provide display coordinates(extrinsic state) at runtime
    robo_dog1 = RoboticFactory.create_robot("ROBOTIC_DOG")
    robo_dog1.display(2, 9)
    robo_dog2 = RoboticFactory.create_robot("ROBOTIC_DOG")
    robo_dog2.display(11, 19)

    # Total robots created: 2 - because we are reusing the same object
    print("Total robots created: " + str(RoboticFactory.get_total_robots()))


if __name__ == "__main__":
    main()
