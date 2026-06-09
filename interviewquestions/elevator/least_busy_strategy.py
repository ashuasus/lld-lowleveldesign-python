from interviewquestions.elevator.elevator_selection_strategy import ElevatorSelectionStrategy

class LeastBusyStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, controllers, request_floor, direction):
        best = None
        min_load = float('inf')

        for controller in controllers:
            load = len(controller.up_min_pq) + len(controller.down_max_pq)
            if load < min_load:
                min_load = load
                best = controller

        return best
