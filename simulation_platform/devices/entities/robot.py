from dataclasses import dataclass

from simulation_platform.lib.entity_base import Entity


@dataclass
class Battery(Entity):
    capacity: float = 56
    power: float = 0.08
    levle: float = 100


@dataclass
class Chassis(Entity):
    speed: float = 0
    x: float = 0
    y: float = 0
    angle: float = 0
