from datetime import date
from .car import Car
from .engine.capulet_engine import CapuletEngine
from .engine.sternman_engine import SternmanEngine
from .engine.willoughby_engine import WilloughbyEngine
from .battery.nubbin_battery import NubbinBattery
from .battery.spindle_battery import SpindleBattery


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        new_engine = CapuletEngine(current_mileage, last_service_mileage)
        new_battery = SpindleBattery(last_service_date)

        new_car: Car = Car(new_engine, new_battery)
        return new_car

    @staticmethod
    def create_glissasde(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        new_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        new_battery = SpindleBattery(last_service_date)

        new_car: Car = Car(new_engine, new_battery)
        return new_car

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_is_on: bool
    ) -> Car:
        new_engine = SternmanEngine(warning_light_is_on)
        new_battery = SpindleBattery(last_service_date)

        new_car: Car = Car(new_engine, new_battery)
        return new_car

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        new_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        new_battery = NubbinBattery(last_service_date)

        new_car: Car = Car(new_engine, new_battery)
        return new_car

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        new_engine = CapuletEngine(current_mileage, last_service_mileage)
        new_battery = NubbinBattery(last_service_date)

        new_car: Car = Car(new_engine, new_battery)
        return new_car
