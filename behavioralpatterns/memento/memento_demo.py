from .application_configuration import ApplicationConfiguration
from .configuration_manager import ConfigurationManager


# Demo Usage
def main():
    print("\n###### Memento Design Pattern ######")

    # Create Originator Object
    app_config = ApplicationConfiguration("Light", 12, True, "English")

    # Create Caretaker Object
    configuration_manager = ConfigurationManager()

    # Default State
    print("\n===> State 1: ")
    configuration_manager.save_state(app_config)  # Default State

    # State 2
    app_config.set_theme("Dark")
    app_config.set_font_size(14)
    print("\n===> State 2: ")
    configuration_manager.save_state(app_config)

    # State 3
    app_config.set_theme("Midnight Blue")
    app_config.set_font_size(16)
    app_config.set_language("Spanish")
    print("\n===> State 3: ")
    configuration_manager.save_state(app_config)

    # Undo 1
    print("\n===> Undo 1 ")
    configuration_manager.undo(app_config)

    # Undo 2
    print("\n===> Undo 2: ")
    configuration_manager.undo(app_config)

    # Undo 3: Try to undo when no history
    print("\n===> Undo 3: ")
    configuration_manager.undo(app_config)  # Default State


if __name__ == "__main__":
    main()
