from .dog import Dog
from .fish import Fish
from .tree import Tree
from .lung_breathing import LungBreathing
from .gill_breathing import GillBreathing
from .photosynthesis import Photosynthesis


# Client Usage
def main():
    print("======= Bridge Design Pattern - Solution Demo ======")

    dog = Dog(LungBreathing())
    fish = Fish(GillBreathing())
    tree = Tree(Photosynthesis())

    dog.breathe()
    fish.breathe()
    tree.breathe()


if __name__ == "__main__":
    main()
