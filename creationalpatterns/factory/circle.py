from .shape import Shape


# Step 2: Concrete Product classes
class Circle(Shape):
    def compute_area(self):
        print("Inside Circle::compute_area() method.")

    def draw(self):
        print("Inside Circle::draw() method.")
