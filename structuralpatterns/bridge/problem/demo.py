from .dog import Dog
from .fish import Fish
from .whale import Whale
from .tree import Tree


# Client
def main():
    print("======= Bridge Design Pattern - Problem Demo ======")
    dog = Dog()
    dog.breathe()
    fish = Fish()
    fish.breathe()
    whale = Whale()
    whale.breathe()
    tree = Tree()
    tree.breathe()


if __name__ == "__main__":
    main()
