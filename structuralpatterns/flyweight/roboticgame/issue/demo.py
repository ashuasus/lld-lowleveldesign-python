from .sprites import Sprites
from .robot import Robot


# Client Code - Robotic game creating robots
def main():
    x = 0
    y = 0
    # Create 5L Humanoid robots
    for i in range(500000):
        humanoid_sprite = Sprites()
        humanoid_robot_object = Robot(x + i, y + i, "HUMANOID", humanoid_sprite)
    # Create 50L Robotic Dog robots
    for i in range(500000):
        robotic_dog_sprite = Sprites()
        robotic_dog_object = Robot(x + i, y + i, "ROBOTIC_DOGS", robotic_dog_sprite)
    # A total of 10L robots created will result in 10L Sprite objects created
    # which will consume a lot of memory.


if __name__ == "__main__":
    main()
