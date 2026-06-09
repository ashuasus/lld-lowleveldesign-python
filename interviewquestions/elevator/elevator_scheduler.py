class ElevatorScheduler:
    def __init__(self, controllers, strategy):
        self._controllers = controllers
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def assign_elevator(self, floor, direction):
        return self._strategy.select_elevator(self._controllers, floor, direction)
