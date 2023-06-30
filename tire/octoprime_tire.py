from abc import ABC
from .tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, sensor_reading: list[int]):
        if len(sensor_reading) != 4:
            print()
            raise IndexError
        for i in sensor_reading:
            if not 0 <= i <= 1:
                raise ValueError
        self.sensor_reading = sensor_reading

    def needs_service(self) -> bool:
        sum = 0
        for i in self.sensor_reading:
            sum += i
        if sum >= 3:
            return True
        else:
            return False
