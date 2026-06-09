class ExternalDispatcher:
    def __init__(self, scheduler):
        self._scheduler = scheduler

    def submit_external_request(self, floor, direction):
        controller = self._scheduler.assign_elevator(floor, direction)
        controller.submit_request(floor)
