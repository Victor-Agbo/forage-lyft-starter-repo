from abc import ABC, abstractmethod
from .engine.engine import Engine
from .battery.battery import Battery
from .tire.tire import Tire


class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine: Engine = engine
        self.battery: Battery = battery
        self.tire: Tire = tire

    @abstractmethod
    def needs_service(self):
        pass
