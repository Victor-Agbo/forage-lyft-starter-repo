from abc import ABC
from datetime import date
from .battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date: date = last_service_date

    def needs_service(self) -> bool:
        if date.today().year - self.last_service_date.year >= 4:
            return True
        else:
            return False
