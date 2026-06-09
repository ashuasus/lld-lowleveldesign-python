from interviewquestions.elevator.floor import Floor

class Building:
    def __init__(self, total_floors, dispatcher):
        self.floors = [Floor(i, dispatcher) for i in range(1, total_floors + 1)]

    def get_floor(self, floor):
        return self.floors[floor - 1]
