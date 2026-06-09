from .mouse import Mouse


# Low-level module - concrete implementation
class BluetoothMouse(Mouse):
    def __init__(self, connection_type, company, model_version, color):
        self.connection_type = connection_type
        self.company = company
        self.model_version = model_version
        self.color = color

    def get_specifications(self):
        print("===> Bluetooth Mouse")
        print("Connection Type: " + self.connection_type)
        print("Company: " + self.company)
        print("Model Version: " + self.model_version)
        print("Color: " + self.color)
