from abc import ABC, abstractmethod


# Step 1: Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def print_contents(self):
        pass
