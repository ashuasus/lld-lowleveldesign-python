from interviewquestions.elevator.elevator_selection_strategy import ElevatorSelectionStrategy
from interviewquestions.elevator.enums.elevator_direction import ElevatorDirection

class NearestElevatorStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, controllers, request_floor, direction):
        best = None
        min_distance = float('inf')

        for controller in controllers:
            next_floor_stoppage = controller.elevator_car.next_floor_stoppage

            is_same_direction_candidate = (
                controller.elevator_car.moving_direction == direction and
                (
                    (direction == ElevatorDirection.UP and next_floor_stoppage <= request_floor) or
                    (direction == ElevatorDirection.DOWN and next_floor_stoppage >= request_floor)
                )
            )

            dist = abs(next_floor_stoppage - request_floor)
            if is_same_direction_candidate and dist < min_distance:
                min_distance = dist
                best = controller

        # Fallback: pick an idle elevator
        if best is None:
            for controller in controllers:
                if controller.elevator_car.moving_direction == ElevatorDirection.IDLE:
                    best = controller
                    break

        # Last resort: pick first elevator
        if best is None:
            best = controllers[0]

        return best
