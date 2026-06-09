from interviewquestions.elevator.internal_dispatcher import InternalDispatcher

class InternalButton:
    def __init__(self, controller):
        self._controller = controller

    def press_button(self, destination_floor):
        InternalDispatcher.get_instance().submit_internal_request(destination_floor, self._controller)
