from simulation_platform.tasks.entities.simulation_task import SimulationTask


class SimulationTaskUseCases:
    def __init__(self) -> None:
        pass

    def query_simulation_task(self, page_index: int = 1, page_size: int = 10):
        pass

    def create_simulation_task(self, simulation_task: SimulationTask):
        pass

    def start_simulation_task(task_id: str):
        pass
