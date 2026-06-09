from .file_system_component import FileSystemComponent


# Step 3: Composite - Folder
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.directory_name = name
        self.children = []

    def add(self, file_system_component):
        self.children.append(file_system_component)

    def remove(self, file_system_component):
        self.children.remove(file_system_component)

    def print_contents(self):
        print("Directory Name: " + self.directory_name)
        for child in self.children:
            child.print_contents()
