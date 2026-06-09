# Caretaker class - manages mementos
class ConfigurationManager:
    def __init__(self):
        self._history = []

    def save_state(self, app_config):
        configuration_memento = app_config.save()  # creates a memento with current state
        self._history.append(configuration_memento)  # stores the memento in the history
        print("[+] State saved. History size: " + str(len(self._history)))
        print(("[+] Default State: " if len(self._history) == 1 else "[+] Current State: ") + str(configuration_memento))

    def undo(self, app_config):
        if len(self._history) > 1:
            self._history.pop()  # removes and returns the last saved state
            memento_to_be_restored = self._history[-1]  # returns the previous state to be restored
            app_config.restore(memento_to_be_restored)  # restores the application configuration
            print("[+] Undo performed. History size: " + str(len(self._history)))
            print(("[+] Default State: " if len(self._history) == 1 else "[+] Current State: ") + str(memento_to_be_restored))
        else:
            print("[+] No more states to undo!")
            print("[+] Default State: " + str(self._history[-1]))
