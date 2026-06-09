from .abstract_expression import AbstractExpression


# Non-terminal Expression - represents multiplication
class MultiplyNonTerminalExpression(AbstractExpression):
    def __init__(self, left, right):
        self.left_expression = left
        self.right_expression = right

    def interpret(self, context):
        return self.left_expression.interpret(context) * self.right_expression.interpret(context)
