import time
from interviewquestions.elevator.elevator_car import ElevatorCar
from interviewquestions.elevator.elevator_controller import ElevatorController
from interviewquestions.elevator.internal_button import InternalButton
from interviewquestions.elevator.elevator_scheduler import ElevatorScheduler
from interviewquestions.elevator.external_dispatcher import ExternalDispatcher
from interviewquestions.elevator.nearest_elevator_strategy import NearestElevatorStrategy
from interviewquestions.elevator.building import Building

def main():
    # 1. Create elevator cars and their controllers
    car1 = ElevatorCar(1)
    controller1 = ElevatorController(car1)

    car2 = ElevatorCar(2)
    controller2 = ElevatorController(car2)

    # 2. Create internal buttons for each elevator
    internal_button_elevator1 = InternalButton(controller1)
    internal_button_elevator2 = InternalButton(controller2)

    # 3. Create scheduler with nearest strategy
    scheduler = ElevatorScheduler([controller1, controller2], NearestElevatorStrategy())

    # 4. Create external dispatcher
    external_dispatcher = ExternalDispatcher(scheduler)

    # 5. Create a 5-floor building
    building = Building(5, external_dispatcher)

    # 6. Start both elevator controller threads
    controller1.start()
    controller2.start()

    # Submit requests
    building.get_floor(3).press_up_button()
    time.sleep(0.005)

    building.get_floor(5).press_down_button()
    time.sleep(0.005)

    internal_button_elevator1.press_button(4)
    time.sleep(0.005)

    internal_button_elevator1.press_button(5)
    time.sleep(0.005)

    building.get_floor(1).press_down_button()
    time.sleep(0.005)

    building.get_floor(2).press_up_button()
    time.sleep(0.005)

    internal_button_elevator1.press_button(2)

    # Wait for threads to finish processing
    time.sleep(2)

if __name__ == "__main__":
    main()
