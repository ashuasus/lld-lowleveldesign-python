from .file import File


class Directory:
    def __init__(self, name):
        self.directory_name = name
        self.object_list = []

    def add(self, obj):
        self.object_list.append(obj)

    def remove(self, obj):
        self.object_list.remove(obj)

    # Display full structure
    # Breaks OCP - if we want to add a new file type, we need to modify this method
    def print_contents(self):
        print("Directory Name: " + self.directory_name)
        for obj in self.object_list:
            if isinstance(obj, File):
                obj.print_contents()
            elif isinstance(obj, Directory):
                obj.print_contents()
