from .chef_tasks import ChefTasks


# GOOD: This class follows ISP
# Now classes only implement what they actually need - Clean implementations
class Chef(ChefTasks):
    def prepare_food(self):
        print("Preparing food...")

    def decide_menu(self):
        print("Deciding menu...")
