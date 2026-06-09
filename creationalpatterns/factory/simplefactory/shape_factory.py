from ..shape_type import ShapeType
from ..circle import Circle
from ..rectangle import Rectangle
from ..square import Square


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type is None:
            return None
        if shape_type == ShapeType.CIRCLE:
            return Circle()
        elif shape_type == ShapeType.RECTANGLE:
            return Rectangle()
        elif shape_type == ShapeType.SQUARE:
            return Square()
        else:
            raise ValueError("ShapeType doesn't exist.")
