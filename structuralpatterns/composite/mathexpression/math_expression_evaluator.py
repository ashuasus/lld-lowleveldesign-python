from .number import Number
from .expression import Expression
from .operation_type import OperationType


# Client Code with Composite Pattern
def main():
    print("======= Composite Design Pattern ======")
    # 2*(1+7) tree structure for evaluation
    two = Number(2)
    one = Number(1)
    seven = Number(7)

    add_expression = Expression(one, seven, OperationType.ADD)
    parent_expression = Expression(two, add_expression, OperationType.MULTIPLY)

    print(parent_expression.evaluate())


if __name__ == "__main__":
    main()
