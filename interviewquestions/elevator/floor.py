from interviewquestions.elevator.external_button import ExternalButton
from interviewquestions.elevator.enums.elevator_direction import ElevatorDirection

class Floor:
    def __init__(self, floor_number, dispatcher):
        self.floor_number = floor_number
        self.up_button = ExternalButton(dispatcher)
        self.down_button = ExternalButton(dispatcher)

    def press_up_button(self):
        self.up_button.press_button(self.floor_number, ElevatorDirection.UP)

    def press_down_button(self):
        self.down_button.press_button(self.floor_number, ElevatorDirection.DOWN)
