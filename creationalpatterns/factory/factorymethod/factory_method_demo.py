from ..shape_type import ShapeType
from .circle_creator import CircleCreator
from .rectangle_creator import RectangleCreator
from .square_creator import SquareCreator


# Step 5: Client code demonstration
def main():
    print("======= Factory Method Design Pattern ======")

    # set the type you want
    shape_type = ShapeType.SQUARE
    # get the shape
    shape = get_shape_instance(shape_type)
    # perform operations
    shape.draw()
    shape.compute_area()


def get_shape_instance(shape_type):
    shape = None
    if shape_type is None:
        return None
    if shape_type == ShapeType.CIRCLE:
        circle_creator = CircleCreator()
        shape = circle_creator.create_shape()
    elif shape_type == ShapeType.RECTANGLE:
        rectangle_creator = RectangleCreator()
        shape = rectangle_creator.create_shape()
    elif shape_type == ShapeType.SQUARE:
        square_creator = SquareCreator()
        shape = square_creator.create_shape()
    else:
        raise ValueError("ShapeType doesn't exist.")
    return shape


if __name__ == "__main__":
    main()
