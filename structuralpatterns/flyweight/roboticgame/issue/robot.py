# Robot class - Used to create Humanoid and Robotic Dog robots
class Robot:
    def __init__(self, coordinate_x, coordinate_y, robot_type, body):
        # extrinsic data
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        # intrinsic data
        self.type = robot_type
        self.body = body  # heavy-weight object - 2D bitmap image
