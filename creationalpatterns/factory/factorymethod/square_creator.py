from .shape_factory import ShapeFactory
from ..square import Square


# Step 4: Concrete Creator classes
class SquareCreator(ShapeFactory):
    def create_shape(self):
        return Square()
