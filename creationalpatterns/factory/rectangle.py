from .shape import Shape


# Step 2: Concrete Product classes
class Rectangle(Shape):
    def compute_area(self):
        print("Inside Rectangle::compute_area() method.")

    def draw(self):
        print("Inside Rectangle::draw() method.")
