from .shape_factory import ShapeFactory
from ..circle import Circle


# Step 4: Concrete Creator classes
class CircleCreator(ShapeFactory):
    def create_shape(self):
        return Circle()
