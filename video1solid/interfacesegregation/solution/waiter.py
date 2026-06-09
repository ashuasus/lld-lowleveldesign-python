from .waiter_tasks import WaiterTasks


# GOOD: This class follows ISP
# Now classes only implement what they actually need - Clean implementations
class Waiter(WaiterTasks):
    def serve_food_and_drinks(self):
        print("Serving food and drinks...")

    def take_order(self):
        print("Taking order...")
