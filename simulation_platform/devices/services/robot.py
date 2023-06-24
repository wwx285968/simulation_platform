from threading import Thread
import time
from simulation_platform.devices.entities.robot import Battery, Chassis
from simulation_platform.devices.communication.base import Commucation


class Robot(Thread):
    def __init__(
        self,
        robot_id: str,
        comm: Commucation,
        multiplier: float = 1,
        chassis: Chassis = Chassis(),
        battery: Battery = Battery()
    ) -> None:
        self.robot_id = robot_id
        self.comm = comm
        self.multiplier = multiplier
        self.chassis = chassis
        self.battery = battery

        self.is_stop = False

        super().__init__()

    def update_battery(self):
        pass

    def update_speed(self):
        pass

    def update_location(self):
        pass

    def get_state(self) -> dict:
        return self.chassis.dict() | self.battery.dict()

    def stop(self):
        self.is_stop = True

    def run(self):
        while not self.is_stop:
            self.comm.report_state(self.get_state())
            time.sleep(0.2)
