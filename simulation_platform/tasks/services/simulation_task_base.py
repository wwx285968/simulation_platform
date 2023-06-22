import time
import threading


class SimulationTaskBase(threading.Thread):

    def __init__(self):
        self.is_stop = False
        super().__init__()

    def start_env(self):
        pass

    def config_simulation_task(self):
        pass

    def update_task_status(self):
        time.sleep(1)

    def stop(self):
        self.is_stop = True

    def run(self):
        while not self.is_stop:
            self.update_task_status()
