from dataclasses import dataclass, field
from datetime import datetime

from simulation_platform.lib.entity_base import Entity


@dataclass
class SimulationTask(Entity):
    id: str
    name: str
    simulation_type: str
    task_type: str
    multiplier: float
    status: str
    create_time: datetime = field(default_factory=lambda: datetime.now())
