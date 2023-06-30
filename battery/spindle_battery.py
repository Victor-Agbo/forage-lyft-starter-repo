from abc import ABC
from datetime import date
from .battery import Battery


class SpindleBattery(Battery, ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date: date = last_service_date

    def needs_service(self):
        if date.today().year - self.last_service_date.year >= 2:
            return True
        else:
            return False
