from .shape_factory import ShapeFactory
from ..rectangle import Rectangle


# Step 4: Concrete Creator classes
class RectangleCreator(ShapeFactory):
    def create_shape(self):
        return Rectangle()
