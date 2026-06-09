from datetime import datetime
from ..model.blog import Blog


# Controller class: BlogController
# Acts as a bridge between Model (Blog) and View (BlogView).
class BlogController:
    def __init__(self, view):
        self.view = view
        self.blogs = []  # acts as an in-memory database

    # Add a new blog post
    def add_blog(self, title, content, author):
        blog = Blog(title, content, author, datetime.now())
        self.blogs.append(blog)
        print("[+] Blog added successfully!")

    # Update an existing blog by index
    def update_blog(self, index, new_title, new_content):
        if 0 <= index < len(self.blogs):
            blog = self.blogs[index]
            blog.set_title(new_title)
            blog.set_content(new_content)
            print("[+] Blog updated successfully!")
        else:
            print("[+] Invalid blog index!")

    # Delete a blog post
    def delete_blog(self, index):
        if 0 <= index < len(self.blogs):
            self.blogs.pop(index)
            print("[+] Blog deleted successfully!")
        else:
            print("[+] Invalid blog index!")

    # Display a single blog post
    def show_blog(self, index):
        if 0 <= index < len(self.blogs):
            self.view.display_blog_details(self.blogs[index])
        else:
            print("[+] Invalid blog index!")

    # Display all blogs
    def show_all_blogs(self):
        self.view.display_all_blogs(self.blogs)
