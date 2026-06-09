# View class: BlogView
# Responsible for displaying blog post details in the console.
# No business logic — just formatting and printing.
class BlogView:
    # Display a single blog post
    def display_blog_details(self, blog):
        print("===== Blog Post =====")
        print("Title   : " + blog.get_title())
        print("Author  : " + blog.get_author())
        print("Date    : " + str(blog.get_created_at()))
        print("Content : " + blog.get_content())

    # Display a list of all blog posts
    def display_all_blogs(self, blogs):
        print("===== All Blog Posts =====")
        for blog in blogs:
            print("- " + blog.get_title() + " by " + blog.get_author())
