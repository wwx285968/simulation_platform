from dataclasses import dataclass, field
from datetime import datetime

from simulation_platform.tasks.entities import Entity


@dataclass
class SimulationTask(Entity):
    id: int
    name: str
    simulation_type: str
    task_type: str
    multiplier: float
    status: str
    create_time: datetime = field(default_factory=lambda: datetime.now())
