import heapq
import threading
from interviewquestions.elevator.enums.elevator_direction import ElevatorDirection

class ElevatorController(threading.Thread):
    def __init__(self, elevator_car):
        super().__init__()
        self.elevator_car = elevator_car
        self.up_min_pq = []        # min-heap
        self.down_max_pq = []      # max-heap (stored as negatives)
        self._condition = threading.Condition()
        self.daemon = True

    def submit_request(self, destination_floor):
        self._enqueue_request(destination_floor)

    def _enqueue_request(self, destination_floor):
        print(f"Request details-> destinationFloor: {destination_floor} accepted by elevator:{self.elevator_car.id}")

        with self._condition:
            if destination_floor == self.elevator_car.next_floor_stoppage:
                return

            if destination_floor >= self.elevator_car.next_floor_stoppage:
                if destination_floor not in self.up_min_pq:
                    heapq.heappush(self.up_min_pq, destination_floor)
            else:
                if -destination_floor not in self.down_max_pq:
                    heapq.heappush(self.down_max_pq, -destination_floor)

            self._condition.notify()

    def run(self):
        self._control_elevator()

    def _control_elevator(self):
        while True:
            # Sleep until a request arrives
            with self._condition:
                while not self.up_min_pq and not self.down_max_pq:
                    print(f"elevator:{self.elevator_car.id} is IDLE")
                    self.elevator_car.moving_direction = ElevatorDirection.IDLE
                    self._condition.wait()

            # Drain up queue (ascending order via min-heap)
            while True:
                with self._condition:
                    if not self.up_min_pq:
                        break
                    floor = heapq.heappop(self.up_min_pq)
                print(f"Serving floor: {floor} by elevator:{self.elevator_car.id} currentFloor: {self.elevator_car.current_floor}")
                self.elevator_car.move_elevator(floor)

            # Drain down queue (descending order via max-heap)
            while True:
                with self._condition:
                    if not self.down_max_pq:
                        break
                    floor = -heapq.heappop(self.down_max_pq)
                print(f"Serving floor: {floor} by elevator:{self.elevator_car.id} currentFloor: {self.elevator_car.current_floor}")
                self.elevator_car.move_elevator(floor)
