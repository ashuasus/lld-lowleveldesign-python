from .i_robot import IRobot


# Concrete Flyweight (Class) - implements the Flyweight interface and stores intrinsic state.
class HumanoidRobot(IRobot):
    def __init__(self, robot_type, body):
        # intrinsic data - shared data - common to all objects
        self._type = robot_type
        self._body = body

    def get_type(self):
        return self._type

    def get_body(self):
        return self._body

    def display(self, x, y):
        # use the humanoid sprites object
        # and X and Y coordinate to render the image.
        print("Displaying " + self._type + " at " + str(x) + ", " + str(y))
