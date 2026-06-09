from datetime import datetime


# Model class: Blog - Holds data about a single blog post.
class Blog:
    def __init__(self, title, content, author, created_at):
        self._title = title
        self._content = content
        self._author = author
        self._created_at = created_at

    # Getters and Setters
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_created_at(self):
        return self._created_at

    def set_created_at(self, created_at):
        self._created_at = created_at
