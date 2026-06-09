from ..shape_type import ShapeType
from .shape_factory import ShapeFactory


# Step 3: Simple Factory Demo (Bloated Design)
def main():
    print("======= Simple Factory Design Pattern ======")

    # set the type you want
    shape_type = ShapeType.SQUARE
    # get the shape
    shape = ShapeFactory.create_shape(shape_type)
    shape.draw()
    shape.compute_area()


if __name__ == "__main__":
    main()
