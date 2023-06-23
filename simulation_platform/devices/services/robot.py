from simulation_platform.devices.entities.robot import Battery, Chassis
from simulation_platform.lib.device_base import Device


class Robot(Device):
    def __init__(
        self, robot_id: str, chassis: Chassis = Chassis(), battery: Battery = Battery()
    ) -> None:
        self.robot_id = robot_id
        self.chassis = chassis
        self.battery = battery

    def update_battery(self):
        pass

    def update_speed(self):
        pass

    def update_location(self):
        pass

    def report_state(self) -> dict:
        return self.chassis.dict() | self.battery.dict()
