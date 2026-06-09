from .sprites import Sprites
from .humanoid_robot import HumanoidRobot
from .robotic_dog import RoboticDog


# Flyweight Factory (Class) - creates and manages flyweight objects
class RoboticFactory:
    _robotic_object_cache = {}

    @classmethod
    def create_robot(cls, robot_type):
        if robot_type in cls._robotic_object_cache:
            # if exists, return the cached object.
            return cls._robotic_object_cache[robot_type]
        else:
            # if not exists, create the object and cache it.
            if robot_type == "HUMANOID":
                humanoid_sprite = Sprites()
                humanoid_object = HumanoidRobot(robot_type, humanoid_sprite)
                cls._robotic_object_cache[robot_type] = humanoid_object
                return humanoid_object
            elif robot_type == "ROBOTIC_DOG":
                robotic_dog_sprite = Sprites()
                robotic_dog_object = RoboticDog(robot_type, robotic_dog_sprite)
                cls._robotic_object_cache[robot_type] = robotic_dog_object
                return robotic_dog_object
        raise ValueError("Invalid robot type: " + robot_type)

    @classmethod
    def get_total_robots(cls):
        return len(cls._robotic_object_cache)
