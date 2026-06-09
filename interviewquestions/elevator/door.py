from interviewquestions.elevator.enums.door_state import DoorState

class Door:
    def __init__(self):
        self.door_state = DoorState.DOOR_CLOSED

    def open_door(self, id):
        self.door_state = DoorState.DOOR_OPEN
        print(f"Opening the Elevator door of elevator:{id}")

    def close_door(self, id):
        self.door_state = DoorState.DOOR_CLOSED
        print(f"Closing the Elevator door of elevator:{id}")
