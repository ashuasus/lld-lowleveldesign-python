from .file_system_component import FileSystemComponent


# Step 2: Leaf - File
class File(FileSystemComponent):
    def __init__(self, name):
        self.file_name = name

    def print_contents(self):
        print("File name: " + self.file_name)
