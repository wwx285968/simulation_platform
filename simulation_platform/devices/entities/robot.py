from dataclasses import dataclass

from simulation_platform.lib.entity_base import Entity


@dataclass
class Battery(Entity):
    capacity: float = 56
