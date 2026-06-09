from .abstract_expression import AbstractExpression


# Non Terminal Expression - represents an expression with a binary operator + or *
class BinaryNonTerminalExpression(AbstractExpression):
    def __init__(self, left_expression, right_expression, operator):
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operator = operator

    def interpret(self, context):
        if self.operator == '+':
            return self.left_expression.interpret(context) + self.right_expression.interpret(context)
        elif self.operator == '*':
            return self.left_expression.interpret(context) * self.right_expression.interpret(context)
        return 0
