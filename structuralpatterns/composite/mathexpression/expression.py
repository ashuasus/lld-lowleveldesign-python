from .arithmetic_expression import ArithmeticExpression
from .operation_type import OperationType


# Composite
class Expression(ArithmeticExpression):
    def __init__(self, left_part, right_part, operation):
        self.left_expression = left_part
        self.right_expression = right_part
        self.operation = operation

    def evaluate(self):
        value = 0
        if self.operation == OperationType.ADD:
            value = self.left_expression.evaluate() + self.right_expression.evaluate()
        elif self.operation == OperationType.SUBTRACT:
            value = self.left_expression.evaluate() - self.right_expression.evaluate()
        elif self.operation == OperationType.DIVIDE:
            value = self.left_expression.evaluate() // self.right_expression.evaluate()
        elif self.operation == OperationType.MULTIPLY:
            value = self.left_expression.evaluate() * self.right_expression.evaluate()

        print("Expression value is:" + str(value))
        return value
