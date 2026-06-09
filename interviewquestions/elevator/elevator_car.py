import time
from interviewquestions.elevator.enums.elevator_direction import ElevatorDirection
from interviewquestions.elevator.door import Door

class ElevatorCar:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.next_floor_stoppage = 0
        self.moving_direction = ElevatorDirection.IDLE
        self.door = Door()

    def show_display(self):
        print(f"elevator:{self.id} Current floor: {self.current_floor} going: {self.moving_direction.value}")

    def move_elevator(self, destination_floor):
        self.next_floor_stoppage = destination_floor
        if self.current_floor == self.next_floor_stoppage:
            self.door.open_door(self.id)
            return

        start_floor = self.current_floor
        self.door.close_door(self.id)

        if self.next_floor_stoppage >= self.current_floor:
            self.moving_direction = ElevatorDirection.UP
            self.show_display()
            for i in range(start_floor + 1, self.next_floor_stoppage + 1):
                time.sleep(0.005)
                self.set_current_floor(i)
                self.show_display()
        else:
            self.moving_direction = ElevatorDirection.DOWN
            self.show_display()
            for i in range(start_floor - 1, self.next_floor_stoppage - 1, -1):
                time.sleep(0.005)
                self.set_current_floor(i)
                self.show_display()

        self.door.open_door(self.id)

    def set_current_floor(self, floor):
        self.current_floor = floor
