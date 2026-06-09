from .abstract_expression import AbstractExpression


# Terminal Expression - represents a variable
class NumberTerminalExpression(AbstractExpression):
    def __init__(self, string_val):
        self.string_value = string_val

    def interpret(self, context):
        return context.get_variable(self.string_value)
