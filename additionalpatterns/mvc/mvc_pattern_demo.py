from additionalpatterns.mvc.controller.blog_controller import BlogController
from additionalpatterns.mvc.view.blog_view import BlogView


def main():
    print("\n ###### MVC Pattern Demo ###### \n")
    view = BlogView()
    controller = BlogController(view)
    controller.add_blog("MVC Pattern in Java", "Learn how to structure Java apps using MVC.", "Alice")
    controller.add_blog("Understanding Design Patterns", "Design patterns make your code reusable and clean.", "Bob")
    controller.add_blog("Java Collections Framework", "Learn about different collections and their use cases.", "Charlie")
    controller.show_all_blogs()
    controller.show_blog(0)
    controller.update_blog(0, "MVC Pattern in Java - Updated", "Updated content for the MVC post.")
    controller.show_blog(0)
    controller.delete_blog(1)
    controller.show_all_blogs()


if __name__ == "__main__":
    main()
