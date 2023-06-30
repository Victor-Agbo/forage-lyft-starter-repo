from abc import ABC
from .tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, sensor_reading: list[int]):
        if len(sensor_reading) != 4:
            raise IndexError
        for i in sensor_reading:
            if not 0 <= i <= 1:
                raise ValueError

        self.sensor_reading = sensor_reading

    def needs_service(self) -> bool:
        for i in self.sensor_reading:
            if i >= 0.9:
                return True

        return False
