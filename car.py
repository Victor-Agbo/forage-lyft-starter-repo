from abc import ABC, abstractmethod
from .engine.engine import Engine
from .battery.battery import Battery


class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine: Engine = engine
        self.battery: Battery = engine

    @abstractmethod
    def needs_service(self):
        pass
