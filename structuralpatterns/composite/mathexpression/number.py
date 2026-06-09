from .arithmetic_expression import ArithmeticExpression


# Leaf
class Number(ArithmeticExpression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        print("Number value is: " + str(self.value))
        return self.value
