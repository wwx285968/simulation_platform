import threading
import time

from simulation_platform.lib.device_base import Device


class Simulation(threading.Thread):
    def __init__(self, multiplier: float = 1):
        self.multiplier = multiplier
        self.devices: dict[str, Device] = {}

    def add_device(self, device_id: str, device: Device):
        self.devices[device_id] = device

    def delete_device(self, device_id: str):
        self.devices.pop(device_id, None)

    def run(self):
        for dev in self.devices.values():
            dev.report_state()
        time.sleep(0.2)
