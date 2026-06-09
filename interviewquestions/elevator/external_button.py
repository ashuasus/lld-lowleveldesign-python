class ExternalButton:
    def __init__(self, dispatcher):
        self._dispatcher = dispatcher

    def press_button(self, floor, direction):
        self._dispatcher.submit_external_request(floor, direction)
