from .shape import Shape


# Step 2: Concrete Product classes
class Square(Shape):
    def compute_area(self):
        print("Inside Square::compute_area() method.")

    def draw(self):
        print("Inside Square::draw() method.")
