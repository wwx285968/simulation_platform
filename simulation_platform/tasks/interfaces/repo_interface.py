from abc import ABC, abstractmethod
from tasks.entities.simulation_task import SimulationTask


class RepoInterfaces(ABC):
    @abstractmethod
    def query_simulation_tasks(
        self,
        page_index: int = 1,
        page_size: int = 10
    ) -> list[SimulationTask]:
        pass
