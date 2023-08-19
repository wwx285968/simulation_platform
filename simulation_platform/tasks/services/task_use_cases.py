from tasks.entities.simulation_task import SimulationTask
from tasks.interfaces.repo_interface import RepoInterfaces


class SimulationTaskUseCases:
    def __init__(self, repo: RepoInterfaces) -> None:
        self.repo = repo

    def query_simulation_task(self, page_index: int = 1, page_size: int = 10) -> list:
        return self.repo.query_simulation_tasks(
            page_index=page_index, page_size=page_size
        )

    def create_simulation_task(
        self, simulation_task: SimulationTask
    ) -> tuple[bool, str]:
        pass

    def delete_simulation_task(self, task_id: str) -> tuple[bool, str]:
        pass

    def start_simulation_task(self, task_id: str) -> tuple[bool, str]:
        pass
