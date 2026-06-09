from .context import Context
from .number_terminal_expression import NumberTerminalExpression
from .add_non_terminal_expression import AddNonTerminalExpression
from .multiply_non_terminal_expression import MultiplyNonTerminalExpression
from .binary_non_terminal_expression import BinaryNonTerminalExpression


# Client code
def main():
    print("##### Interpreter Design Pattern #####")

    # Context
    context = Context()
    context.set_variable("a", 12)
    context.set_variable("b", 5)
    context.set_variable("c", 3)
    context.set_variable("d", 9)
    print("Context: " + str(context))

    # Expression: a + b
    expression1 = AddNonTerminalExpression(
        NumberTerminalExpression("a"),
        NumberTerminalExpression("b"))
    print("Expression: (a+b) = " + str(expression1.interpret(context)))  # Output: 17

    # Expression: a * b
    expression2 = MultiplyNonTerminalExpression(
        NumberTerminalExpression("a"),
        NumberTerminalExpression("b")
    )
    print("Expression: (a*b) = " + str(expression2.interpret(context)))  # Output: 60

    # Complex Expression: (a + b) * c
    expression3 = MultiplyNonTerminalExpression(
        AddNonTerminalExpression(
            NumberTerminalExpression("a"),
            NumberTerminalExpression("b")
        ),
        NumberTerminalExpression("c")
    )
    print("Expression: ((a+b)*c) = " + str(expression3.interpret(context)))  # Output: 51

    # Expression: ((a*b) + (c*d))
    expression4 = BinaryNonTerminalExpression(
        BinaryNonTerminalExpression(
            NumberTerminalExpression("a"), NumberTerminalExpression("b"), '*'),
        BinaryNonTerminalExpression(
            NumberTerminalExpression("c"), NumberTerminalExpression("d"), '*'),
        '+')
    print("Expression: ((a*b) + (c*d)) = " + str(expression4.interpret(context)))


if __name__ == "__main__":
    main()
