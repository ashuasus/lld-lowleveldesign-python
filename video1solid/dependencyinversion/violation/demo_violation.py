from ..utility.wired_keyboard import WiredKeyboard
from ..utility.wired_mouse import WiredMouse
from ..utility.bluetooth_keyboard import BluetoothKeyboard
from ..utility.bluetooth_mouse import BluetoothMouse
from .mac_book import MacBook


def main():
    # create keyboard and mouse objects
    wired_keyboard = WiredKeyboard("USB", "Dell", "F602", "Grey")
    wired_mouse = WiredMouse("USB", "Dell", "F602", "Grey")
    bluetooth_keyboard = BluetoothKeyboard("Bluetooth", "Logitech", "G102", "Black")
    bluetooth_mouse = BluetoothMouse("Bluetooth", "Logitech", "G102", "Black")

    # create macbook
    mac_book_with_wired_parts = MacBook(wired_keyboard, wired_mouse)
    mac_book_with_wired_parts.get_keyboard().get_specifications()
    mac_book_with_wired_parts.get_mouse().get_specifications()

    # create macbook with bluetooth keyboard and mouse
    # mac_book_with_bluetooth_parts = MacBook(bluetooth_keyboard, bluetooth_keyboard)
    # cannot create macbook with bluetooth keyboard and mouse because
    # macbook depends on wired keyboard and mouse - tight coupling - violation of DIP


if __name__ == "__main__":
    main()
